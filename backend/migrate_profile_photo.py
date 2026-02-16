#!/usr/bin/env python3
"""
Migration script to add profile_photo column to users table.
This script should be run on the production environment (Render).
"""

import sys
import os
sys.path.append('.')

from sqlalchemy import text
from app.database import engine

def migrate_profile_photo():
    """Add profile_photo column to users table if it doesn't exist."""
    
    try:
        with engine.connect() as connection:
            # Check if column already exists
            result = connection.execute(text("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = 'users' AND column_name = 'profile_photo'
            """))
            
            if result.fetchone():
                print("✅ profile_photo column already exists in users table")
                return True
            
            # Add the column
            print("📝 Adding profile_photo column to users table...")
            connection.execute(text("""
                ALTER TABLE users 
                ADD COLUMN profile_photo TEXT
            """))
            
            connection.commit()
            print("✅ profile_photo column added successfully!")
            return True
            
    except Exception as e:
        print(f"❌ Error during migration: {e}")
        return False

if __name__ == "__main__":
    success = migrate_profile_photo()
    if not success:
        sys.exit(1)
