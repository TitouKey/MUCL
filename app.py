import os
import re
from datetime import datetime

from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
    flash,
    session,
)
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    current_user,
    login_required,
)
from werkzeug.routing import BaseConverter
from werkzeug.security import generate_password_hash

from models import (
    Crew,
    Member,
    PartnerSchool,
    Research,
    Sponsor,
    Subscriber,
    User,
    Log,
    db,
    CATEGORIES,
    CATEGORY_COLORS,
)

from translations import FR, LANGUAGES

DEFAULT_LANG = "en"
_LANG_ENDPOINTS = set()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
INSTANCE_FOLDER = os.path.join(BASE_DIR, "instance")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-me-in-production")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(INSTANCE_FOLDER, "mars.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(INSTANCE_FOLDER, exist_ok=True)

db.init_app(app)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"


class LangConverter(BaseConverter):
    regex = "|".join(sorted(LANGUAGES.keys()))


app.url_map.converters["lang"] = LangConverter


# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def log_action(action, entity_type, entity_id=None, details=""):
    """Log user actions for auditing"""
    if hasattr(g, 'user') and g.user:
        user_id = g.user.id
    elif current_user.is_authenticated:
        user_id = current_user.id
    else:
        user_id = None
    
    ip = request.remote_addr or ""
    user_agent = request.user_agent.string if hasattr(request, 'user_agent') else ""
    
    log = Log(
        user_id=user_id,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        details=details,
        ip_address=ip,
        user_agent=user_agent
    )
    db.session.add(log)
    db.session.commit()


def get_client_ip():
    """Get client IP address"""
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0]
    return request.remote_addr or ""


@app.template_global()
def static_exists(path):
    return os.path.exists(os.path.join(app.static_folder, path))


@app.before_request
def set_language():
    lang = DEFAULT_LANG
    first = request.path.lstrip("/").split("/", 1)[0]
    if first in LANGUAGES:
        lang = first
    g.lang = lang


@app.url_defaults
def add_lang_default(endpoint, values):
    if endpoint in _LANG_ENDPOINTS and "lang" not in values:
        values["lang"] = getattr(g, "lang", DEFAULT_LANG)


@app.url_value_preprocessor
def pop_lang(endpoint, values):
    if values and "lang" in values:
        values.pop("lang")


def lang_route(rule, **options):
    def decorator(view):
        endpoint = options.pop("endpoint", None) or view.__name__
        prefixed = "/<lang:lang>" + (rule if rule.startswith("/") else "/" + rule)

        def _redirect_default():
            return redirect(url_for(endpoint, lang=DEFAULT_LANG))

        app.add_url_rule(prefixed, endpoint=endpoint, view_func=view, **options)
        app.add_url_rule(rule, endpoint=endpoint + "__nolang", view_func=_redirect_default, **options)
        _LANG_ENDPOINTS.add(endpoint)
        return view

    return decorator


CREW_PHOTOS = {
    "crew-190": "img/crews/UCLtoMARS18/crew-photo.webp",
    "crew-212": "img/crews/UCLtoMARS19/crew-photo.jpg",
    "crew-227": "img/crews/UCLtoMARS20-21/crew-photo.jpg",
    "tharsis-crew": "img/crews/Tharsis/crew-photo.webp",
    "ares-crew": "img/crews/Ares/crew-photo.jpg",
    "atlas-crew": "img/crews/Atlas/crew-photo.webp",
    "syrtis-crew": "img/crews/Syrtis/crew-photo.webp",
    "arsia-crew": "img/crews/Arsia/crew-photo.webp",
}


CREW_PHOTO_OPTS = {
    "syrtis-crew": {"y": "40%"},
    "atlas-crew": {"y": "17%"},
    "ares-crew": {"y": "45%"},
    "tharsis-crew": {"y": "40%"},
    "crew-227": {"y": "45%"},
    "crew-212": {"y": "55%", "zoom": "115%"},
}


@app.context_processor
def inject_i18n():
    def t(key):
        if g.lang == "fr":
            return FR.get(key, key)
        return key

    def tr(obj, field):
        val = getattr(obj, field, "") or ""
        if g.lang == "fr":
            fr_val = getattr(obj, field + "_fr", None)
            if fr_val:
                return fr_val
        return val

    def lang_switch_url(code):
        if request.endpoint in _LANG_ENDPOINTS:
            view_args = dict(request.view_args or {})
            url = url_for(request.endpoint, lang=code, **view_args)
            if request.query_string:
                url += "?" + request.query_string.decode()
            return url
        return "/" + code + "/"

    def crew_photo(crew):
        if crew.slug in CREW_PHOTOS:
            return url_for("static", filename=CREW_PHOTOS[crew.slug])
        if crew.photo:
            return url_for("uploaded_file", filename=crew.photo)
        return None

    def crew_photo_position(crew):
        opts = CREW_PHOTO_OPTS.get(crew.slug)
        return opts["y"] if opts else None

    def crew_photo_size(crew):
        opts = CREW_PHOTO_OPTS.get(crew.slug)
        return opts.get("zoom") if opts else None

    return {"t": t, "tr": tr, "lang": g.lang, "LANGUAGES": LANGUAGES, "lang_switch_url": lang_switch_url, "crew_photo": crew_photo, "crew_photo_position": crew_photo_position, "crew_photo_size": crew_photo_size, "CATEGORIES": CATEGORIES, "CATEGORY_COLORS": CATEGORY_COLORS}


# ---------------------------------------------------------------------------
# Authentication routes
# ---------------------------------------------------------------------------


@app.before_request
def before_request():
    g.user = current_user


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin_dashboard"))
    
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        remember = request.form.get("remember") == "on"
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password) and user.is_active:
            login_user(user, remember=remember)
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            log_action("login", "user", user.id, f"User {username} logged in")
            
            next_page = request.args.get("next")
            return redirect(next_page or url_for("admin_dashboard"))
        else:
            flash("Invalid username or password", "error")
    
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    log_action("logout", "user", current_user.id, f"User {current_user.username} logged out")
    logout_user()
    return redirect(url_for("index"))


# ---------------------------------------------------------------------------
# Admin routes
# ---------------------------------------------------------------------------


@app.route("/admin")
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    # Statistics
    crew_count = Crew.query.count()
    member_count = Member.query.count()
    research_count = Research.query.count()
    sponsor_count = Sponsor.query.count()
    user_count = User.query.count()
    
    # Recent logs
    recent_logs = Log.query.order_by(Log.created_at.desc()).limit(20).all()
    
    return render_template(
        "admin/dashboard.html",
        active="admin",
        crew_count=crew_count,
        member_count=member_count,
        research_count=research_count,
        sponsor_count=sponsor_count,
        user_count=user_count,
        recent_logs=recent_logs,
        current_user=current_user
    )


# ---------------------------------------------------------------------------
# CRUD routes for Crews
# ---------------------------------------------------------------------------


@app.route("/admin/crews")
@login_required
def admin_crews():
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    crews = Crew.query.order_by(Crew.order_index.desc(), Crew.year.desc()).all()
    return render_template("admin/crews.html", active="admin", crews=crews)


@app.route("/admin/crews/add", methods=["GET", "POST"])
@app.route("/admin/crews/edit/<int:crew_id>", methods=["GET", "POST"])
@login_required
def admin_crew_edit(crew_id=None):
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    crew = Crew.query.get(crew_id) if crew_id else None
    
    if request.method == "POST":
        if crew:
            crew.name = request.form.get("name", "")
            crew.slug = request.form.get("slug", "")
            crew.year = request.form.get("year", "")
            crew.is_current = request.form.get("is_current") == "on"
            crew.tagline = request.form.get("tagline", "")
            crew.tagline_fr = request.form.get("tagline_fr", "")
            crew.description = request.form.get("description", "")
            crew.description_fr = request.form.get("description_fr", "")
            crew.order_index = int(request.form.get("order_index", 0))
            
            action = "update"
            message = "Crew updated successfully"
        else:
            crew = Crew(
                name=request.form.get("name", ""),
                slug=request.form.get("slug", ""),
                year=request.form.get("year", ""),
                is_current=request.form.get("is_current") == "on",
                tagline=request.form.get("tagline", ""),
                tagline_fr=request.form.get("tagline_fr", ""),
                description=request.form.get("description", ""),
                description_fr=request.form.get("description_fr", ""),
                order_index=int(request.form.get("order_index", 0))
            )
            db.session.add(crew)
            action = "create"
            message = "Crew created successfully"
        
        db.session.commit()
        log_action(action, "crew", crew.id, f"Crew {crew.name} {action}d")
        flash(message, "success")
        return redirect(url_for("admin_crews"))
    
    return render_template("admin/crew_edit.html", active="admin", crew=crew)


@app.route("/admin/crews/delete/<int:crew_id>", methods=["POST"])
@login_required
def admin_crew_delete(crew_id):
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    crew = Crew.query.get(crew_id)
    if crew:
        db.session.delete(crew)
        db.session.commit()
        log_action("delete", "crew", crew_id, f"Crew {crew.name} deleted")
        flash("Crew deleted successfully", "success")
    return redirect(url_for("admin_crews"))


# ---------------------------------------------------------------------------
# CRUD routes for Members
# ---------------------------------------------------------------------------


@app.route("/admin/members")
@login_required
def admin_members():
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    members = Member.query.order_by(Member.order_index.asc()).all()
    crews = Crew.query.order_by(Crew.name).all()
    return render_template("admin/members.html", active="admin", members=members, crews=crews)


@app.route("/admin/members/add", methods=["GET", "POST"])
@app.route("/admin/members/edit/<int:member_id>", methods=["GET", "POST"])
@login_required
def admin_member_edit(member_id=None):
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    member = Member.query.get(member_id) if member_id else None
    crews = Crew.query.order_by(Crew.name).all()
    
    if request.method == "POST":
        crew_id = request.form.get("crew_id")
        crew_id = int(crew_id) if crew_id and crew_id != "" else None
        
        if member:
            member.crew_id = crew_id
            member.name = request.form.get("name", "")
            member.slug = request.form.get("slug", "")
            member.role = request.form.get("role", "")
            member.role_fr = request.form.get("role_fr", "")
            member.studies = request.form.get("studies", "")
            member.studies_fr = request.form.get("studies_fr", "")
            member.nationality = request.form.get("nationality", "BE")
            member.nation = request.form.get("nation", "")
            member.description = request.form.get("description", "")
            member.description_fr = request.form.get("description_fr", "")
            member.socials = request.form.get("socials", "[]")
            member.order_index = int(request.form.get("order_index", 0))
            
            action = "update"
            message = "Member updated successfully"
        else:
            member = Member(
                crew_id=crew_id,
                name=request.form.get("name", ""),
                slug=request.form.get("slug", ""),
                role=request.form.get("role", ""),
                role_fr=request.form.get("role_fr", ""),
                studies=request.form.get("studies", ""),
                studies_fr=request.form.get("studies_fr", ""),
                nationality=request.form.get("nationality", "BE"),
                nation=request.form.get("nation", ""),
                description=request.form.get("description", ""),
                description_fr=request.form.get("description_fr", ""),
                socials=request.form.get("socials", "[]"),
                order_index=int(request.form.get("order_index", 0))
            )
            db.session.add(member)
            action = "create"
            message = "Member created successfully"
        
        db.session.commit()
        log_action(action, "member", member.id, f"Member {member.name} {action}d")
        flash(message, "success")
        return redirect(url_for("admin_members"))
    
    return render_template("admin/member_edit.html", active="admin", member=member, crews=crews)


@app.route("/admin/members/delete/<int:member_id>", methods=["POST"])
@login_required
def admin_member_delete(member_id):
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    member = Member.query.get(member_id)
    if member:
        db.session.delete(member)
        db.session.commit()
        log_action("delete", "member", member_id, f"Member {member.name} deleted")
        flash("Member deleted successfully", "success")
    return redirect(url_for("admin_members"))


# ---------------------------------------------------------------------------
# CRUD routes for Research
# ---------------------------------------------------------------------------


@app.route("/admin/researches")
@login_required
def admin_researches():
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    researches = Research.query.order_by(Research.order_index.asc(), Research.year.desc()).all()
    return render_template("admin/researches.html", active="admin", researches=researches)


@app.route("/admin/researches/add", methods=["GET", "POST"])
@app.route("/admin/researches/edit/<int:research_id>", methods=["GET", "POST"])
@login_required
def admin_research_edit(research_id=None):
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    research = Research.query.get(research_id) if research_id else None
    crews = Crew.query.order_by(Crew.name).all()
    members = Member.query.order_by(Member.name).all()
    sponsors = Sponsor.query.order_by(Sponsor.name).all()
    
    if request.method == "POST":
        crew_id = request.form.get("crew_id")
        crew_id = int(crew_id) if crew_id and crew_id != "" else None
        
        if research:
            research.title = request.form.get("title", "")
            research.title_fr = request.form.get("title_fr", "")
            research.slug = request.form.get("slug", "")
            research.authors = request.form.get("authors", "")
            research.year = request.form.get("year", "")
            research.mission = request.form.get("mission", "")
            research.mission_fr = request.form.get("mission_fr", "")
            research.crew_id = crew_id
            research.disciplines = request.form.get("disciplines", "[]")
            research.description = request.form.get("description", "")
            research.description_fr = request.form.get("description_fr", "")
            research.category = request.form.get("category", "science")
            research.links = request.form.get("links", "[]")
            research.order_index = int(request.form.get("order_index", 0))
            
            action = "update"
            message = "Research updated successfully"
        else:
            research = Research(
                title=request.form.get("title", ""),
                title_fr=request.form.get("title_fr", ""),
                slug=request.form.get("slug", ""),
                authors=request.form.get("authors", ""),
                year=request.form.get("year", ""),
                mission=request.form.get("mission", ""),
                mission_fr=request.form.get("mission_fr", ""),
                crew_id=crew_id,
                disciplines=request.form.get("disciplines", "[]"),
                description=request.form.get("description", ""),
                description_fr=request.form.get("description_fr", ""),
                category=request.form.get("category", "science"),
                links=request.form.get("links", "[]"),
                order_index=int(request.form.get("order_index", 0))
            )
            db.session.add(research)
            action = "create"
            message = "Research created successfully"
        
        db.session.commit()
        log_action(action, "research", research.id, f"Research {research.title} {action}d")
        flash(message, "success")
        return redirect(url_for("admin_researches"))
    
    return render_template("admin/research_edit.html", active="admin", research=research, crews=crews, members=members, sponsors=sponsors)


@app.route("/admin/researches/delete/<int:research_id>", methods=["POST"])
@login_required
def admin_research_delete(research_id):
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    research = Research.query.get(research_id)
    if research:
        db.session.delete(research)
        db.session.commit()
        log_action("delete", "research", research_id, f"Research {research.title} deleted")
        flash("Research deleted successfully", "success")
    return redirect(url_for("admin_researches"))


# ---------------------------------------------------------------------------
# CRUD routes for Sponsors
# ---------------------------------------------------------------------------


@app.route("/admin/sponsors")
@login_required
def admin_sponsors():
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    sponsors = Sponsor.query.order_by(Sponsor.priority.asc(), Sponsor.id.asc()).all()
    return render_template("admin/sponsors.html", active="admin", sponsors=sponsors)


@app.route("/admin/sponsors/add", methods=["GET", "POST"])
@app.route("/admin/sponsors/edit/<int:sponsor_id>", methods=["GET", "POST"])
@login_required
def admin_sponsor_edit(sponsor_id=None):
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    sponsor = Sponsor.query.get(sponsor_id) if sponsor_id else None
    
    if request.method == "POST":
        if sponsor:
            sponsor.name = request.form.get("name", "")
            sponsor.full_name = request.form.get("full_name", "")
            sponsor.full_name_fr = request.form.get("full_name_fr", "")
            sponsor.slug = request.form.get("slug", "")
            sponsor.website = request.form.get("website", "")
            sponsor.priority = int(request.form.get("priority", 100))
            sponsor.has_page = request.form.get("has_page") == "on"
            sponsor.logo_light = request.form.get("logo_light") == "on"
            sponsor.description = request.form.get("description", "")
            sponsor.description_fr = request.form.get("description_fr", "")
            sponsor.support = request.form.get("support", "")
            sponsor.support_fr = request.form.get("support_fr", "")
            
            action = "update"
            message = "Sponsor updated successfully"
        else:
            sponsor = Sponsor(
                name=request.form.get("name", ""),
                full_name=request.form.get("full_name", ""),
                full_name_fr=request.form.get("full_name_fr", ""),
                slug=request.form.get("slug", ""),
                website=request.form.get("website", ""),
                priority=int(request.form.get("priority", 100)),
                has_page=request.form.get("has_page") == "on",
                logo_light=request.form.get("logo_light") == "on",
                description=request.form.get("description", ""),
                description_fr=request.form.get("description_fr", ""),
                support=request.form.get("support", ""),
                support_fr=request.form.get("support_fr", "")
            )
            db.session.add(sponsor)
            action = "create"
            message = "Sponsor created successfully"
        
        db.session.commit()
        log_action(action, "sponsor", sponsor.id, f"Sponsor {sponsor.name} {action}d")
        flash(message, "success")
        return redirect(url_for("admin_sponsors"))
    
    return render_template("admin/sponsor_edit.html", active="admin", sponsor=sponsor)


@app.route("/admin/sponsors/delete/<int:sponsor_id>", methods=["POST"])
@login_required
def admin_sponsor_delete(sponsor_id):
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    sponsor = Sponsor.query.get(sponsor_id)
    if sponsor:
        db.session.delete(sponsor)
        db.session.commit()
        log_action("delete", "sponsor", sponsor_id, f"Sponsor {sponsor.name} deleted")
        flash("Sponsor deleted successfully", "success")
    return redirect(url_for("admin_sponsors"))


# ---------------------------------------------------------------------------
# User management routes
# ---------------------------------------------------------------------------


@app.route("/admin/users")
@login_required
def admin_users():
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    users = User.query.order_by(User.username).all()
    return render_template("admin/users.html", active="admin", users=users)


@app.route("/admin/users/add", methods=["GET", "POST"])
@app.route("/admin/users/edit/<int:user_id>", methods=["GET", "POST"])
@login_required
def admin_user_edit(user_id=None):
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    user = User.query.get(user_id) if user_id else None
    
    if request.method == "POST":
        username = request.form.get("username", "")
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        is_admin = request.form.get("is_admin") == "on"
        is_active = request.form.get("is_active") == "on"
        
        if user:
            user.username = username
            user.email = email
            if password:
                user.set_password(password)
            user.is_admin = is_admin
            user.is_active = is_active
            
            action = "update"
            message = "User updated successfully"
        else:
            user = User(
                username=username,
                email=email,
                is_admin=is_admin,
                is_active=is_active
            )
            user.set_password(password)
            db.session.add(user)
            action = "create"
            message = "User created successfully"
        
        db.session.commit()
        log_action(action, "user", user.id, f"User {username} {action}d")
        flash(message, "success")
        return redirect(url_for("admin_users"))
    
    return render_template("admin/user_edit.html", active="admin", user=user)


@app.route("/admin/users/delete/<int:user_id>", methods=["POST"])
@login_required
def admin_user_delete(user_id):
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    user = User.query.get(user_id)
    if user and user.id != current_user.id:  # Cannot delete self
        db.session.delete(user)
        db.session.commit()
        log_action("delete", "user", user_id, f"User {user.username} deleted")
        flash("User deleted successfully", "success")
    return redirect(url_for("admin_users"))


# ---------------------------------------------------------------------------
# Logs management routes
# ---------------------------------------------------------------------------


@app.route("/admin/logs")
@login_required
def admin_logs():
    if not current_user.is_admin:
        return redirect(url_for("index"))
    
    page = request.args.get("page", 1, type=int)
    per_page = 50
    
    logs = Log.query.order_by(Log.created_at.desc()).paginate(page=page, per_page=per_page)
    return render_template("admin/logs.html", active="admin", logs=logs)


# ---------------------------------------------------------------------------
# Public pages
# ---------------------------------------------------------------------------


@lang_route("/")
def index():
    research_count = Research.query.count()
    crews = Crew.query.order_by(Crew.order_index.desc(), Crew.year.desc()).all()
    current_crew = next((c for c in crews if c.is_current), crews[0] if crews else None)
    return render_template(
        "index.html",
        active="index",
        research_count=research_count,
        current_crew=current_crew,
    )


@lang_route("/mission")
def mission():
    return render_template("mission.html", active="mission")


@lang_route("/crew")
def crew_page():
    crews = Crew.query.order_by(Crew.order_index.desc(), Crew.year.desc()).all()
    current_crew = next((c for c in crews if c.is_current), crews[0] if crews else None)
    return render_template("crew.html", active="crew", crews=crews, current_crew=current_crew)


@lang_route("/crew/<slug>")
def crew_detail(slug):
    crew = Crew.query.filter_by(slug=slug).first_or_404()
    researches = crew.researches.order_by(Research.order_index.asc()).all() if crew.researches else []
    return render_template("crew_detail.html", active="crew", crew=crew, researches=researches)


@lang_route("/research")
def research():
    query = Research.query.order_by(Research.order_index.asc(), Research.year.desc())
    crew = None
    crew_slug = request.args.get("crew")
    if crew_slug:
        crew = Crew.query.filter_by(slug=crew_slug).first()
        if crew:
            query = Research.query.filter_by(crew_id=crew.id).order_by(Research.order_index.asc())
    researches = query.all()
    research_count = Research.query.count()
    return render_template(
        "research.html",
        active="research",
        researches=researches,
        research_count=research_count,
        crew=crew,
    )


@lang_route("/education")
def education():
    schools = PartnerSchool.query.order_by(PartnerSchool.order_index.asc()).all()
    return render_template("education.html", active="education", schools=schools)


@lang_route("/sponsors")
def sponsors():
    sponsors = Sponsor.query.order_by(Sponsor.priority.asc(), Sponsor.id.asc()).all()
    return render_template("sponsors.html", active="sponsors", sponsors=sponsors)


@lang_route("/partner/<slug>")
def partner(slug):
    sponsor = Sponsor.query.filter_by(slug=slug).first_or_404()
    return render_template("partner.html", active="sponsors", sponsor=sponsor)


@lang_route("/brochure")
def brochure():
    return render_template("brochure.html", active="brochure")


@lang_route("/brochure-sponsors")
def sponsor_brochure():
    return render_template("sponsor_brochure.html", active="brochure")


@lang_route("/legal")
def legal():
    return render_template("legal.html", active="legal")


@lang_route("/support")
def support():
    hall_names = []
    return render_template("support.html", active="support", hall_names=hall_names)


_EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


@lang_route("/newsletter", methods=["POST"])
def newsletter():
    email = (request.form.get("email") or "").strip().lower()

    def _t(key):
        return FR.get(key, key) if g.lang == "fr" else key

    if not email or not _EMAIL_RE.match(email):
        return {"ok": False, "message": _t("Please enter a valid email address.")}, 400

    if not Subscriber.query.filter_by(email=email).first():
        db.session.add(Subscriber(email=email, lang=g.lang))
        db.session.commit()

    return {"ok": True, "message": _t("Thank you for subscribing! You will hear from us soon.")}


@lang_route("/contact")
def contact():
    return render_template("contact.html", active="contact")


@lang_route("/join")
def join():
    return render_template("join.html", active="join")


@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# ---------------------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------------------


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
