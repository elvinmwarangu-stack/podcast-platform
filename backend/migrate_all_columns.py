#!/usr/bin/env python3
"""
Comprehensive migration script to add all missing columns to the users table.
This script handles profile_photo, reset_token, and reset_token_expires columns.
"""

import sys
sys.path.append('.')

from sqlalchemy import text
from app.database import engine

def migrate_all_columns():
    """Add all missing columns to users table."""
    
    migrations = [
        {
            "name": "profile_photo",
            "sql": "ALTER TABLE users ADD COLUMN profile_photo TEXT"
        },
        {
            "name": "role", 
            "sql": "ALTER TABLE users ADD COLUMN role VARCHAR(50) NOT NULL DEFAULT 'user'"
        },
        {
            "name": "reset_token", 
            "sql": "ALTER TABLE users ADD COLUMN reset_token VARCHAR(255)"
        },
        {
            "name": "reset_token_expires",
            "sql": "ALTER TABLE users ADD COLUMN reset_token_expires TIMESTAMP WITH TIME ZONE"
        }
    ]
    
    try:
        with engine.connect() as connection:
            # Start a transaction
            with connection.begin():
                # Check if users table exists first
                result = connection.execute(text("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_name = 'users'
                    )
                """))
                table_exists = result.scalar()
                
                if not table_exists:
                    print("⚠️  Users table doesn't exist yet. Skipping migrations.")
                    return True
                
                # Get existing columns
                result = connection.execute(text("""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_name = 'users'
                """))
                existing_columns = {row[0] for row in result.fetchall()}
                
                print(f"📋 Existing columns: {sorted(existing_columns)}")
                
                # Add missing columns
                for migration in migrations:
                    column_name = migration["name"]
                    if column_name not in existing_columns:
                        print(f"📝 Adding {column_name} column to users table...")
                        connection.execute(text(migration["sql"]))
                        print(f"✅ {column_name} column added successfully!")
                    else:
                        print(f"✅ {column_name} column already exists")
                
                print("🎉 All migrations completed successfully!")
                return True
            
    except Exception as e:
        print(f"❌ Error during migration: {e}")
        return False

if __name__ == "__main__":
    success = migrate_all_columns()
    if not success:
        sys.exit(1)
