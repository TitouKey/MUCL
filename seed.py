"""Seed the database with the research catalogue only.

Crews, members, sponsors and partner schools are left empty so they can
be created one by one from the admin area.

Run:  flask --app app seed   (or:  python seed.py)
"""

from app import app, slugify
from models import Admin, Research, db
from research_data import RESEARCH_DATA


def seed_researches():
    used_slugs = set()

    for i, e in enumerate(RESEARCH_DATA):
        base = slugify(e["title"])
        slug, n = base, 2
        while slug in used_slugs:
            slug = f"{base}-{n}"
            n += 1
        used_slugs.add(slug)
        db.session.add(
            Research(
                title=e["title"],
                slug=slug,
                authors=e.get("authors", ""),
                year=e.get("year", ""),
                mission=e.get("crew", ""),
                category=e.get("category", "science"),
                links=e.get("links", []),
                disciplines=e.get("disciplines", []),
                description=e.get("description", ""),
                order_index=i,
            )
        )


def run():
    with app.app_context():
        db.drop_all()
        db.create_all()

        from werkzeug.security import generate_password_hash

        admin = Admin(username="admin", password_hash=generate_password_hash("mars-admin"))
        db.session.add(admin)

        seed_researches()

        db.session.commit()

        print("Seeded:")
        print(f"  researches: {Research.query.count()}")
        print("Crews, members, sponsors and schools are empty — create them from the admin area.")
        print("Admin account: admin / mars-admin")


if __name__ == "__main__":
    run()
