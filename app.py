import os
import re

from flask import (
    Flask,
    flash,
    g,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from models import (
    Admin,
    Crew,
    Experience,
    Member,
    PartnerSchool,
    Research,
    Sponsor,
    Subscriber,
    db,
)

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
login_manager.login_view = 'admin_login'

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


# Helper function for slug generation
def slugify(text):
    import re
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text


# Allowed file extensions for uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.template_global()
def static_exists(path):
    return os.path.exists(os.path.join(app.static_folder, path))


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
def inject_globals():
    def t(key):
        return key

    def tr(obj, field):
        val = getattr(obj, field, "") or ""
        return val

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

    return {"t": t, "tr": tr, "lang": "en", "crew_photo": crew_photo, "crew_photo_position": crew_photo_position, "crew_photo_size": crew_photo_size}


# ---------------------------------------------------------------------------
# Public pages
# ---------------------------------------------------------------------------


@app.route("/")
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


@app.route("/mission")
def mission():
    return render_template("mission.html", active="mission")


@app.route("/crew")
def crew_page():
    crews = Crew.query.order_by(Crew.order_index.desc(), Crew.year.desc()).all()
    current_crew = next((c for c in crews if c.is_current), crews[0] if crews else None)
    return render_template("crew.html", active="crew", crews=crews, current_crew=current_crew)


@app.route("/crew/<slug>")
def crew_detail(slug):
    crew = Crew.query.filter_by(slug=slug).first_or_404()
    researches = crew.researches.order_by(Research.order_index.asc()).all() if crew.researches else []
    return render_template("crew_detail.html", active="crew", crew=crew, researches=researches)


@app.route("/research")
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


@app.route("/education")
def education():
    schools = PartnerSchool.query.order_by(PartnerSchool.order_index.asc()).all()
    return render_template("education.html", active="education", schools=schools)


@app.route("/sponsors")
def sponsors():
    sponsors = Sponsor.query.order_by(Sponsor.priority.asc(), Sponsor.id.asc()).all()
    return render_template("sponsors.html", active="sponsors", sponsors=sponsors)


@app.route("/partner/<slug>")
def partner(slug):
    sponsor = Sponsor.query.filter_by(slug=slug).first_or_404()
    return render_template("partner.html", active="sponsors", sponsor=sponsor)


@app.route("/brochure")
def brochure():
    return render_template("brochure.html", active="brochure")


@app.route("/legal")
def legal():
    return render_template("legal.html", active="legal")


@app.route("/support")
def support():
    hall_names = []
    return render_template("support.html", active="support", hall_names=hall_names)


_EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


@app.route("/newsletter", methods=["POST"])
def newsletter():
    email = (request.form.get("email") or "").strip().lower()

    if not email or not _EMAIL_RE.match(email):
        return {"ok": False, "message": "Please enter a valid email address."}, 400

    if not Subscriber.query.filter_by(email=email).first():
        db.session.add(Subscriber(email=email, lang="en"))
        db.session.commit()

    return {"ok": True, "message": "Thank you for subscribing! You will hear from us soon."}


@app.route("/contact")
def contact():
    return render_template("contact.html", active="contact")


@app.route("/join")
def join():
    return render_template("join.html", active="join")


@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# ---------------------------------------------------------------------------
# Admin Routes
# ---------------------------------------------------------------------------


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = Admin.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid username or password", "error")
    
    return render_template("admin/login.html")


@app.route("/admin/logout")
@login_required
def admin_logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for('admin_login'))


@app.route("/admin/")
@login_required
def admin_dashboard():
    crew_count = Crew.query.count()
    member_count = Member.query.count()
    sponsor_count = Sponsor.query.count()
    school_count = PartnerSchool.query.count()
    research_count = Research.query.count()
    experience_count = Experience.query.count()
    
    return render_template(
        "admin/dashboard.html",
        crew_count=crew_count,
        member_count=member_count,
        sponsor_count=sponsor_count,
        school_count=school_count,
        research_count=research_count,
        experience_count=experience_count
    )


# Crew CRUD
@app.route("/admin/crews/")
@login_required
def admin_crews():
    crews = Crew.query.order_by(Crew.order_index.desc(), Crew.year.desc()).all()
    return render_template("admin/crews.html", crews=crews)


@app.route("/admin/crews/add", methods=["GET", "POST"])
@login_required
def admin_crews_add():
    if request.method == "POST":
        name = request.form.get("name")
        slug = request.form.get("slug") or slugify(name)
        year = request.form.get("year", "")
        is_current = request.form.get("is_current") == "on"
        tagline = request.form.get("tagline", "")
        description = request.form.get("description", "")
        order_index = int(request.form.get("order_index", 0))
        
        photo = None
        if 'photo' in request.files:
            file = request.files['photo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                photo = f"crew-{slug}-{filename}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], photo))
        
        crew = Crew(
            name=name,
            slug=slug,
            year=year,
            is_current=is_current,
            tagline=tagline,
            description=description,
            photo=photo,
            order_index=order_index
        )
        db.session.add(crew)
        db.session.commit()
        flash("Crew added successfully!", "success")
        return redirect(url_for('admin_crews'))
    
    return render_template("admin/crew_form.html", crew=None)


@app.route("/admin/crews/<int:id>/edit", methods=["GET", "POST"])
@login_required
def admin_crews_edit(id):
    crew = Crew.query.get_or_404(id)
    
    if request.method == "POST":
        crew.name = request.form.get("name")
        crew.slug = request.form.get("slug") or slugify(crew.name)
        crew.year = request.form.get("year", "")
        crew.is_current = request.form.get("is_current") == "on"
        crew.tagline = request.form.get("tagline", "")
        crew.description = request.form.get("description", "")
        crew.order_index = int(request.form.get("order_index", 0))
        
        if 'photo' in request.files:
            file = request.files['photo']
            if file and allowed_file(file.filename):
                if crew.photo:
                    old_path = os.path.join(app.config["UPLOAD_FOLDER"], crew.photo)
                    if os.path.exists(old_path):
                        os.remove(old_path)
                filename = secure_filename(file.filename)
                crew.photo = f"crew-{crew.slug}-{filename}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], crew.photo))
        
        db.session.commit()
        flash("Crew updated successfully!", "success")
        return redirect(url_for('admin_crews'))
    
    return render_template("admin/crew_form.html", crew=crew)


@app.route("/admin/crews/<int:id>/delete", methods=["POST"])
@login_required
def admin_crews_delete(id):
    crew = Crew.query.get_or_404(id)
    
    if crew.photo:
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], crew.photo)
        if os.path.exists(photo_path):
            os.remove(photo_path)
    
    db.session.delete(crew)
    db.session.commit()
    flash("Crew deleted successfully!", "success")
    return redirect(url_for('admin_crews'))


# Member CRUD
@app.route("/admin/members/")
@login_required
def admin_members():
    members = Member.query.order_by(Member.crew_id, Member.order_index).all()
    crews = Crew.query.order_by(Crew.name).all()
    return render_template("admin/members.html", members=members, crews=crews)


@app.route("/admin/members/add", methods=["GET", "POST"])
@login_required
def admin_members_add():
    crews = Crew.query.order_by(Crew.name).all()
    
    if request.method == "POST":
        name = request.form.get("name")
        slug = request.form.get("slug") or slugify(name)
        crew_id = request.form.get("crew_id")
        role = request.form.get("role", "")
        studies = request.form.get("studies", "")
        nationality = request.form.get("nationality", "BE")
        nation = request.form.get("nation", "")
        description = request.form.get("description", "")
        order_index = int(request.form.get("order_index", 0))
        
        socials = []
        for i in range(1, 6):
            platform = request.form.get(f"social_platform_{i}")
            url = request.form.get(f"social_url_{i}")
            if platform and url:
                socials.append({"platform": platform, "url": url})
        
        photo = None
        if 'photo' in request.files:
            file = request.files['photo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                photo = f"member-{slug}-{filename}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], photo))
        
        member = Member(
            name=name,
            slug=slug,
            crew_id=int(crew_id) if crew_id else None,
            role=role,
            studies=studies,
            nationality=nationality,
            nation=nation,
            description=description,
            photo=photo,
            socials=socials,
            order_index=order_index
        )
        db.session.add(member)
        db.session.commit()
        flash("Member added successfully!", "success")
        return redirect(url_for('admin_members'))
    
    return render_template("admin/member_form.html", member=None, crews=crews)


@app.route("/admin/members/<int:id>/edit", methods=["GET", "POST"])
@login_required
def admin_members_edit(id):
    member = Member.query.get_or_404(id)
    crews = Crew.query.order_by(Crew.name).all()
    
    if request.method == "POST":
        member.name = request.form.get("name")
        member.slug = request.form.get("slug") or slugify(member.name)
        member.crew_id = int(request.form.get("crew_id")) if request.form.get("crew_id") else None
        member.role = request.form.get("role", "")
        member.studies = request.form.get("studies", "")
        member.nationality = request.form.get("nationality", "BE")
        member.nation = request.form.get("nation", "")
        member.description = request.form.get("description", "")
        member.order_index = int(request.form.get("order_index", 0))
        
        socials = []
        for i in range(1, 6):
            platform = request.form.get(f"social_platform_{i}")
            url = request.form.get(f"social_url_{i}")
            if platform and url:
                socials.append({"platform": platform, "url": url})
        member.socials = socials
        
        if 'photo' in request.files:
            file = request.files['photo']
            if file and allowed_file(file.filename):
                if member.photo:
                    old_path = os.path.join(app.config["UPLOAD_FOLDER"], member.photo)
                    if os.path.exists(old_path):
                        os.remove(old_path)
                filename = secure_filename(file.filename)
                member.photo = f"member-{member.slug}-{filename}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], member.photo))
        
        db.session.commit()
        flash("Member updated successfully!", "success")
        return redirect(url_for('admin_members'))
    
    return render_template("admin/member_form.html", member=member, crews=crews)


@app.route("/admin/members/<int:id>/delete", methods=["POST"])
@login_required
def admin_members_delete(id):
    member = Member.query.get_or_404(id)
    
    if member.photo:
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], member.photo)
        if os.path.exists(photo_path):
            os.remove(photo_path)
    
    db.session.delete(member)
    db.session.commit()
    flash("Member deleted successfully!", "success")
    return redirect(url_for('admin_members'))


# Sponsor CRUD
@app.route("/admin/sponsors/")
@login_required
def admin_sponsors():
    sponsors = Sponsor.query.order_by(Sponsor.priority, Sponsor.name).all()
    return render_template("admin/sponsors.html", sponsors=sponsors)


@app.route("/admin/sponsors/add", methods=["GET", "POST"])
@login_required
def admin_sponsors_add():
    if request.method == "POST":
        name = request.form.get("name")
        full_name = request.form.get("full_name", "")
        slug = request.form.get("slug") or slugify(name)
        website = request.form.get("website", "")
        priority = int(request.form.get("priority", 100))
        has_page = request.form.get("has_page") == "on"
        logo_light = request.form.get("logo_light") == "on"
        description = request.form.get("description", "")
        support = request.form.get("support", "")
        
        logo = None
        image = None
        
        if 'logo' in request.files:
            file = request.files['logo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                logo = f"sponsor-{slug}-logo-{filename}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], logo))
        
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                image = f"sponsor-{slug}-image-{filename}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], image))
        
        sponsor = Sponsor(
            name=name,
            full_name=full_name,
            slug=slug,
            website=website,
            priority=priority,
            has_page=has_page,
            logo=logo,
            logo_light=logo_light,
            image=image,
            description=description,
            support=support
        )
        db.session.add(sponsor)
        db.session.commit()
        flash("Sponsor added successfully!", "success")
        return redirect(url_for('admin_sponsors'))
    
    return render_template("admin/sponsor_form.html", sponsor=None)


@app.route("/admin/sponsors/<int:id>/edit", methods=["GET", "POST"])
@login_required
def admin_sponsors_edit(id):
    sponsor = Sponsor.query.get_or_404(id)
    
    if request.method == "POST":
        sponsor.name = request.form.get("name")
        sponsor.full_name = request.form.get("full_name", "")
        sponsor.slug = request.form.get("slug") or slugify(sponsor.name)
        sponsor.website = request.form.get("website", "")
        sponsor.priority = int(request.form.get("priority", 100))
        sponsor.has_page = request.form.get("has_page") == "on"
        sponsor.logo_light = request.form.get("logo_light") == "on"
        sponsor.description = request.form.get("description", "")
        sponsor.support = request.form.get("support", "")
        
        if 'logo' in request.files:
            file = request.files['logo']
            if file and allowed_file(file.filename):
                if sponsor.logo:
                    old_path = os.path.join(app.config["UPLOAD_FOLDER"], sponsor.logo)
                    if os.path.exists(old_path):
                        os.remove(old_path)
                filename = secure_filename(file.filename)
                sponsor.logo = f"sponsor-{sponsor.slug}-logo-{filename}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], sponsor.logo))
        
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                if sponsor.image:
                    old_path = os.path.join(app.config["UPLOAD_FOLDER"], sponsor.image)
                    if os.path.exists(old_path):
                        os.remove(old_path)
                filename = secure_filename(file.filename)
                sponsor.image = f"sponsor-{sponsor.slug}-image-{filename}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], sponsor.image))
        
        db.session.commit()
        flash("Sponsor updated successfully!", "success")
        return redirect(url_for('admin_sponsors'))
    
    return render_template("admin/sponsor_form.html", sponsor=sponsor)


@app.route("/admin/sponsors/<int:id>/delete", methods=["POST"])
@login_required
def admin_sponsors_delete(id):
    sponsor = Sponsor.query.get_or_404(id)
    
    if sponsor.logo:
        logo_path = os.path.join(app.config["UPLOAD_FOLDER"], sponsor.logo)
        if os.path.exists(logo_path):
            os.remove(logo_path)
    
    if sponsor.image:
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], sponsor.image)
        if os.path.exists(image_path):
            os.remove(image_path)
    
    db.session.delete(sponsor)
    db.session.commit()
    flash("Sponsor deleted successfully!", "success")
    return redirect(url_for('admin_sponsors'))


# Partner School CRUD
@app.route("/admin/schools/")
@login_required
def admin_schools():
    schools = PartnerSchool.query.order_by(PartnerSchool.order_index, PartnerSchool.name).all()
    return render_template("admin/schools.html", schools=schools)


@app.route("/admin/schools/add", methods=["GET", "POST"])
@login_required
def admin_schools_add():
    if request.method == "POST":
        name = request.form.get("name")
        website = request.form.get("website", "")
        order_index = int(request.form.get("order_index", 0))
        
        logo = None
        if 'logo' in request.files:
            file = request.files['logo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                logo = f"school-{slugify(name)}-logo-{filename}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], logo))
        
        school = PartnerSchool(
            name=name,
            website=website,
            logo=logo,
            order_index=order_index
        )
        db.session.add(school)
        db.session.commit()
        flash("School added successfully!", "success")
        return redirect(url_for('admin_schools'))
    
    return render_template("admin/school_form.html", school=None)


@app.route("/admin/schools/<int:id>/edit", methods=["GET", "POST"])
@login_required
def admin_schools_edit(id):
    school = PartnerSchool.query.get_or_404(id)
    
    if request.method == "POST":
        school.name = request.form.get("name")
        school.website = request.form.get("website", "")
        school.order_index = int(request.form.get("order_index", 0))
        
        if 'logo' in request.files:
            file = request.files['logo']
            if file and allowed_file(file.filename):
                if school.logo:
                    old_path = os.path.join(app.config["UPLOAD_FOLDER"], school.logo)
                    if os.path.exists(old_path):
                        os.remove(old_path)
                filename = secure_filename(file.filename)
                school.logo = f"school-{slugify(school.name)}-logo-{filename}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], school.logo))
        
        db.session.commit()
        flash("School updated successfully!", "success")
        return redirect(url_for('admin_schools'))
    
    return render_template("admin/school_form.html", school=school)


@app.route("/admin/schools/<int:id>/delete", methods=["POST"])
@login_required
def admin_schools_delete(id):
    school = PartnerSchool.query.get_or_404(id)
    
    if school.logo:
        logo_path = os.path.join(app.config["UPLOAD_FOLDER"], school.logo)
        if os.path.exists(logo_path):
            os.remove(logo_path)
    
    db.session.delete(school)
    db.session.commit()
    flash("School deleted successfully!", "success")
    return redirect(url_for('admin_schools'))


# Experience CRUD
@app.route("/admin/experiences/")
@login_required
def admin_experiences():
    experiences = Experience.query.order_by(Experience.order_index.desc(), Experience.year.desc()).all()
    return render_template("admin/experiences.html", experiences=experiences)


@app.route("/admin/experiences/add", methods=["GET", "POST"])
@login_required
def admin_experiences_add():
    crews = Crew.query.order_by(Crew.name).all()
    
    if request.method == "POST":
        title = request.form.get("title")
        slug = request.form.get("slug") or slugify(title)
        description = request.form.get("description", "")
        year = request.form.get("year", "")
        date = request.form.get("date", "")
        crew_id = request.form.get("crew_id")
        category = request.form.get("category", "science")
        order_index = int(request.form.get("order_index", 0))
        
        photo = None
        if 'photo' in request.files:
            file = request.files['photo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                photo = f"experience-{slug}-{filename}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], photo))
        
        gallery = []
        if 'gallery' in request.files:
            files = request.files.getlist('gallery')
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    gallery.append(f"experience-{slug}-gallery-{filename}")
                    file.save(os.path.join(app.config["UPLOAD_FOLDER"], f"experience-{slug}-gallery-{filename}"))
        
        experience = Experience(
            title=title,
            slug=slug,
            description=description,
            year=year,
            date=date,
            crew_id=int(crew_id) if crew_id else None,
            category=category,
            photo=photo,
            gallery=gallery,
            order_index=order_index
        )
        db.session.add(experience)
        db.session.commit()
        flash("Experience added successfully!", "success")
        return redirect(url_for('admin_experiences'))
    
    return render_template("admin/experience_form.html", experience=None, crews=crews)


@app.route("/admin/experiences/<int:id>/edit", methods=["GET", "POST"])
@login_required
def admin_experiences_edit(id):
    experience = Experience.query.get_or_404(id)
    crews = Crew.query.order_by(Crew.name).all()
    
    if request.method == "POST":
        experience.title = request.form.get("title")
        experience.slug = request.form.get("slug") or slugify(experience.title)
        experience.description = request.form.get("description", "")
        experience.year = request.form.get("year", "")
        experience.date = request.form.get("date", "")
        experience.crew_id = int(request.form.get("crew_id")) if request.form.get("crew_id") else None
        experience.category = request.form.get("category", "science")
        experience.order_index = int(request.form.get("order_index", 0))
        
        if 'photo' in request.files:
            file = request.files['photo']
            if file and allowed_file(file.filename):
                if experience.photo:
                    old_path = os.path.join(app.config["UPLOAD_FOLDER"], experience.photo)
                    if os.path.exists(old_path):
                        os.remove(old_path)
                filename = secure_filename(file.filename)
                experience.photo = f"experience-{experience.slug}-{filename}"
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], experience.photo))
        
        gallery = []
        if 'gallery' in request.files:
            files = request.files.getlist('gallery')
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    gallery.append(f"experience-{experience.slug}-gallery-{filename}")
                    file.save(os.path.join(app.config["UPLOAD_FOLDER"], f"experience-{experience.slug}-gallery-{filename}"))
        
        experience.gallery = gallery
        
        db.session.commit()
        flash("Experience updated successfully!", "success")
        return redirect(url_for('admin_experiences'))
    
    return render_template("admin/experience_form.html", experience=experience, crews=crews)


@app.route("/admin/experiences/<int:id>/delete", methods=["POST"])
@login_required
def admin_experiences_delete(id):
    experience = Experience.query.get_or_404(id)
    
    if experience.photo:
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], experience.photo)
        if os.path.exists(photo_path):
            os.remove(photo_path)
    
    if experience.gallery_list:
        for image in experience.gallery_list:
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], image)
            if os.path.exists(image_path):
                os.remove(image_path)
    
    db.session.delete(experience)
    db.session.commit()
    flash("Experience deleted successfully!", "success")
    return redirect(url_for('admin_experiences'))


# ---------------------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------------------


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # Auto-migration: add 'level' column to sponsor table if missing
        inspector = db.inspect(db.engine)
        columns = [col['name'] for col in inspector.get_columns('sponsor')]
        if 'level' not in columns:
            with db.engine.connect() as conn:
                conn.execute(db.text("ALTER TABLE sponsor ADD COLUMN level VARCHAR(40) DEFAULT 'official_partner'"))
                conn.execute(db.text("UPDATE sponsor SET level = 'official_partner' WHERE level IS NULL"))
                conn.commit()
                print("✓ Added 'level' column to sponsor table")
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
