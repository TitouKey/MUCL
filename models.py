from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

CATEGORY_TECH = "tech"
CATEGORY_HEALTH = "health"
CATEGORY_SCIENCE = "science"
CATEGORY_OTHER = "other"

CATEGORIES = [
    (CATEGORY_TECH, "Technology"),
    (CATEGORY_HEALTH, "Health & Biology"),
    (CATEGORY_SCIENCE, "Geology, Physics & Sciences"),
    (CATEGORY_OTHER, "Other"),
]

CATEGORY_COLORS = {
    CATEGORY_TECH: "#ff7a00",
    CATEGORY_HEALTH: "#16a34a",
    CATEGORY_SCIENCE: "#2563eb",
    CATEGORY_OTHER: "#d946ef",
}

research_members = db.Table(
    "research_members",
    db.Column("research_id", db.Integer, db.ForeignKey("research.id"), primary_key=True),
    db.Column("member_id", db.Integer, db.ForeignKey("member.id"), primary_key=True),
)

research_partners = db.Table(
    "research_partners",
    db.Column("research_id", db.Integer, db.ForeignKey("research.id"), primary_key=True),
    db.Column("sponsor_id", db.Integer, db.ForeignKey("sponsor.id"), primary_key=True),
)


class Admin(UserMixin, db.Model):
    __tablename__ = "admin"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)


class Crew(db.Model):
    __tablename__ = "crew"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    year = db.Column(db.String(40), default="")
    is_current = db.Column(db.Boolean, default=False)
    tagline = db.Column(db.Text, default="")
    tagline_fr = db.Column(db.Text, default="")
    description = db.Column(db.Text, default="")
    description_fr = db.Column(db.Text, default="")
    photo = db.Column(db.String(255))
    order_index = db.Column(db.Integer, default=0)

    members = db.relationship(
        "Member",
        backref="crew",
        lazy="dynamic",
        order_by="Member.order_index",
        cascade="all, delete-orphan",
    )
    researches = db.relationship(
        "Research",
        backref="crew_ref",
        lazy="dynamic",
        foreign_keys="Research.crew_id",
    )

    @property
    def member_count(self):
        return self.members.count()

    @property
    def display_name(self):
        return f"{self.name} · {self.year}" if self.year else self.name


class Member(db.Model):
    __tablename__ = "member"

    id = db.Column(db.Integer, primary_key=True)
    crew_id = db.Column(db.Integer, db.ForeignKey("crew.id", ondelete="SET NULL"), nullable=True)
    name = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(120), default="")
    role_fr = db.Column(db.String(120), default="")
    studies = db.Column(db.String(160), default="")
    studies_fr = db.Column(db.String(160), default="")
    nationality = db.Column(db.String(4), default="BE")
    nation = db.Column(db.String(80), default="")
    description = db.Column(db.Text, default="")
    description_fr = db.Column(db.Text, default="")
    photo = db.Column(db.String(255))
    socials = db.Column(db.JSON, default=list)
    order_index = db.Column(db.Integer, default=0)

    @property
    def social_list(self):
        if isinstance(self.socials, list):
            return self.socials
        return []


class Research(db.Model):
    __tablename__ = "research"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    title_fr = db.Column(db.String(300), default="")
    slug = db.Column(db.String(300), unique=True, nullable=False)
    authors = db.Column(db.String(300), default="")
    year = db.Column(db.String(40), default="")
    mission = db.Column(db.String(120), default="")
    mission_fr = db.Column(db.String(120), default="")
    crew_id = db.Column(db.Integer, db.ForeignKey("crew.id", ondelete="SET NULL"), nullable=True)
    disciplines = db.Column(db.JSON, default=list)
    description = db.Column(db.Text, default="")
    description_fr = db.Column(db.Text, default="")
    category = db.Column(db.String(20), default="science")
    links = db.Column(db.JSON, default=list)
    pdf = db.Column(db.String(255))
    order_index = db.Column(db.Integer, default=0)

    members = db.relationship("Member", secondary=research_members, backref="researches")
    partners = db.relationship("Sponsor", secondary=research_partners, backref="researches")

    @property
    def discipline_list(self):
        if isinstance(self.disciplines, list):
            return self.disciplines
        return []

    @property
    def link_list(self):
        if isinstance(self.links, list):
            return self.links
        return []

    @property
    def category_label(self):
        return dict(CATEGORIES).get(self.category, self.category)

    @property
    def display_authors(self):
        names = [m.name for m in self.members]
        if self.authors:
            extras = [a for a in self.authors.split(" · ") if a not in names]
            return " · ".join(names + extras)
        return " · ".join(names) if names else ""


class Sponsor(db.Model):
    __tablename__ = "sponsor"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    full_name = db.Column(db.String(120), default="")
    full_name_fr = db.Column(db.String(120), default="")
    slug = db.Column(db.String(120), unique=True, nullable=False)
    website = db.Column(db.String(255), default="")
    priority = db.Column(db.Integer, default=100)
    logo = db.Column(db.String(255))
    has_page = db.Column(db.Boolean, default=False)
    logo_light = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(255))
    description = db.Column(db.Text, default="")
    description_fr = db.Column(db.Text, default="")
    support = db.Column(db.Text, default="")
    support_fr = db.Column(db.Text, default="")

    @property
    def support_paragraphs(self):
        return [p for p in (self.support or "").split("\n\n") if p.strip()]

    @property
    def support_paragraphs_fr(self):
        return [p for p in (self.support_fr or "").split("\n\n") if p.strip()]

    @property
    def description_paragraphs(self):
        return [p for p in (self.description or "").split("\n\n") if p.strip()]

    @property
    def description_paragraphs_fr(self):
        return [p for p in (self.description_fr or "").split("\n\n") if p.strip()]


class PartnerSchool(db.Model):
    __tablename__ = "partner_school"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    name_fr = db.Column(db.String(120), default="")
    website = db.Column(db.String(255), default="")
    logo = db.Column(db.String(255))
    order_index = db.Column(db.Integer, default=0)


class Subscriber(db.Model):
    __tablename__ = "subscriber"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True, nullable=False)
    lang = db.Column(db.String(5), default="en")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
