import os
import re

from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

from models import (
    Crew,
    PartnerSchool,
    Research,
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
# Error handlers
# ---------------------------------------------------------------------------


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
