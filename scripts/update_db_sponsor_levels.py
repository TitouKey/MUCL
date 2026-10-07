#!/usr/bin/env python3
"""
Script pour mettre à jour la base de données avec la colonne 'level' pour les sponsors
et ajouter des exemples de sponsors pour chaque niveau.

Utilisation:
    python scripts/update_db_sponsor_levels.py

Ce script:
1. Ajoute la colonne 'level' à la table 'sponsor' si elle n'existe pas
2. Met à jour les sponsors existants avec le niveau par défaut 'official_partner'
3. Ajoute des exemples de sponsors pour chaque niveau (y compris Official Support)
"""

import os
import sqlite3
from pathlib import Path

# ============================================================
# Configuration
# ============================================================
BASE_DIR = Path(__file__).parent.parent
INSTANCE_FOLDER = BASE_DIR / "instance"
DB_PATH = INSTANCE_FOLDER / "mars.db"

# S'assurer que le dossier instance existe
INSTANCE_FOLDER.mkdir(exist_ok=True)

# Niveaux de sponsors
SPONSOR_LEVELS = {
    'title_partner': 'Title Partner',
    'main_partner': 'Main Partner',
    'official_partner': 'Official Partner',
    'institutional_partner': 'Institutional Partner',
    'technical_partner': 'Technical Partner',
    'official_support': 'Official Support'
}

# Exemples de sponsors par niveau
SPONSOR_EXAMPLES = {
    'title_partner': [
        {
            'name': 'UCLouvain',
            'slug': 'uclouvain',
            'logo': 'img/sponsors/uclouvain.svg',
            'priority': 1,
            'website': 'https://uclouvain.be',
            'has_page': True
        },
    ],
    'main_partner': [
        {
            'name': 'Sopra Steria',
            'slug': 'sopra-steria',
            'logo': 'img/sponsors/sopra-steria.png',
            'priority': 10,
            'website': 'https://soprasteria.com',
            'has_page': False
        },
        {
            'name': 'Thales',
            'slug': 'thales',
            'logo': 'img/sponsors/thales.png',
            'priority': 20,
            'website': 'https://thalesgroup.com',
            'has_page': False
        },
    ],
    'official_partner': [
        {
            'name': 'Space Applications',
            'slug': 'space-applications',
            'logo': 'img/sponsors/spaceapplications.png',
            'priority': 30,
            'website': 'https://spaceapplications.com',
            'has_page': False
        },
        {
            'name': 'Aerospacelab',
            'slug': 'aerospacelab',
            'logo': 'img/sponsors/aerospacelab.png',
            'priority': 40,
            'website': 'https://aerospacelab.be',
            'has_page': False
        },
    ],
    'institutional_partner': [
        {
            'name': 'Belspo',
            'slug': 'belspo',
            'logo': 'img/sponsors/belspo.png',
            'priority': 60,
            'website': 'https://belspo.be',
            'has_page': False
        },
        {
            'name': 'Wallonie',
            'slug': 'wallonie',
            'logo': 'img/sponsors/wallonie.png',
            'priority': 70,
            'website': 'https://spw.wallonie.be',
            'has_page': False
        },
    ],
    'technical_partner': [
        {
            'name': 'SpaceX',
            'slug': 'spacex',
            'logo': 'img/sponsors/spacex.png',
            'priority': 90,
            'website': 'https://spacex.com',
            'has_page': False
        },
        {
            'name': 'Innovative Sensors',
            'slug': 'innovative-sensors',
            'logo': '',
            'priority': 100,
            'website': '',
            'has_page': False
        },
    ],
    'official_support': [
        {
            'name': 'ESA',
            'slug': 'esa',
            'logo': 'img/sponsors/esa.png',
            'priority': 1,
            'website': 'https://esa.int',
            'has_page': False
        },
        {
            'name': 'Science Infuse',
            'slug': 'science-infuse',
            'logo': 'img/sponsors/science-infuse.png',
            'priority': 2,
            'website': '',
            'has_page': False
        },
        {
            'name': 'CNES',
            'slug': 'cnes',
            'logo': 'img/sponsors/cnes.png',
            'priority': 3,
            'website': 'https://cnes.fr',
            'has_page': False
        },
        {
            'name': 'NASA',
            'slug': 'nasa',
            'logo': 'img/sponsors/nasa.png',
            'priority': 4,
            'website': 'https://nasa.gov',
            'has_page': False
        },
    ]
}


def main():
    """Exécute la migration de la base de données."""
    print("=" * 70)
    print("Mise à jour de la base de données - Niveaux de sponsors")
    print("=" * 70)
    
    # Connexion à la base de données
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    try:
        # ============================================================
        # 1. Ajouter la colonne level si elle n'existe pas
        # ============================================================
        print("\n[1/4] Vérification de la colonne 'level'...")
        cursor.execute("PRAGMA table_info(sponsor)")
        columns = [col[1] for col in cursor.fetchall()]
        
        if 'level' not in columns:
            cursor.execute("ALTER TABLE sponsor ADD COLUMN level VARCHAR(40) DEFAULT 'official_partner'")
            conn.commit()
            print("  ✓ Colonne 'level' ajoutée")
        else:
            print("  ✓ Colonne 'level' existe déjà")
        
        # ============================================================
        # 2. Mettre à jour les sponsors existants
        # ============================================================
        print("\n[2/4] Mise à jour des sponsors existants...")
        cursor.execute("UPDATE sponsor SET level = 'official_partner' WHERE level IS NULL")
        updated_count = cursor.rowcount
        conn.commit()
        print(f"  ✓ {updated_count} sponsors mis à jour avec niveau par défaut 'official_partner'")
        
        # ============================================================
        # 3. Récupérer les slugs existants
        # ============================================================
        print("\n[3/4] Vérification des sponsors existants...")
        cursor.execute("SELECT slug FROM sponsor")
        existing_slugs = {row[0] for row in cursor.fetchall()}
        print(f"  ✓ {len(existing_slugs)} sponsors existants trouvés")
        
        # ============================================================
        # 4. Insérer les exemples de sponsors
        # ============================================================
        print("\n[4/4] Ajout des exemples de sponsors...")
        inserted_count = 0
        for level_id, sponsors in SPONSOR_EXAMPLES.items():
            for sponsor_data in sponsors:
                slug = sponsor_data['slug']
                if slug not in existing_slugs:
                    has_page = sponsor_data.get('has_page', False)
                    cursor.execute("""
                        INSERT INTO sponsor (name, slug, level, logo, website, priority, has_page)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (
                        sponsor_data['name'],
                        slug,
                        level_id,
                        sponsor_data.get('logo', ''),
                        sponsor_data.get('website', ''),
                        sponsor_data.get('priority', 100),
                        has_page
                    ))
                    inserted_count += 1
                    existing_slugs.add(slug)  # Ajouter au set pour éviter les doublons
        
        conn.commit()
        print(f"  ✓ {inserted_count} exemples de sponsors insérés")
        
        # ============================================================
        # 5. Afficher le résultat
        # ============================================================
        print("\n" + "=" * 70)
        print("RÉSULTAT - SPONSORS PAR NIVEAU :")
        print("=" * 70)
        
        total_sponsors = 0
        for level_id, level_name in SPONSOR_LEVELS.items():
            cursor.execute("""
                SELECT name, logo, website, has_page
                FROM sponsor
                WHERE level = ?
                ORDER BY priority ASC
            """, (level_id,))
            
            sponsors = cursor.fetchall()
            total_sponsors += len(sponsors)
            print(f"\n{level_name} ({len(sponsors)} sponsors):")
            for name, logo, website, has_page in sponsors:
                logo_status = "✓" if logo else "✗"
                page_status = " (page)" if has_page else ""
                web_status = f" [{website}]" if website else ""
                print(f"  - {name}{logo_status}{page_status}{web_status}")
        
        print(f"\n{'=' * 70}")
        print(f"TOTAL: {total_sponsors} sponsors dans la base de données")
        print("=" * 70)
        print("\n✅ Migration terminée avec succès !")
        
    except Exception as e:
        conn.rollback()
        print(f"\n❌ Erreur: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
