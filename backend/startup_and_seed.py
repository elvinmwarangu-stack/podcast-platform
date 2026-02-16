#!/usr/bin/env python3
"""
Startup script that runs migrations and then seeds the database.
This ensures the database schema is up to date before seeding.
"""

import sys
sys.path.append('.')

def run_migrations():
    """Run database migrations."""
    try:
        print("🔄 Running database migrations...")
        from migrate_profile_photo import migrate_profile_photo
        success = migrate_profile_photo()
        if not success:
            return False
        print("✅ Migrations completed successfully")
        return True
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False

def seed_database():
    """Seed the database with initial data."""
    try:
        print("🌱 Seeding database...")
        import seed_data
        print("✅ Database seeded successfully")
        return True
    except Exception as e:
        print(f"❌ Seeding failed: {e}")
        return False

def main():
    """Run migrations and seeding."""
    print("🚀 Starting database setup...")
    
    # Run migrations first
    if not run_migrations():
        print("❌ Failed to run migrations. Exiting.")
        sys.exit(1)
    
    # Then seed the database
    if not seed_database():
        print("❌ Failed to seed database. Exiting.")
        sys.exit(1)
    
    print("🎉 Database setup completed successfully!")

if __name__ == "__main__":
    main()
