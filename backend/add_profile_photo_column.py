#!/usr/bin/env python3
"""
Migration script to add the missing profile_photo column to the users table.
Run this script to fix the database schema mismatch.
"""

import sys
sys.path.append('.')

from sqlalchemy import text
from app.database import engine

def add_profile_photo_column():
    """Add profile_photo column to users table if it doesn't exist."""
    
    with engine.connect() as connection:
        # Check if column already exists
        result = connection.execute(text("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'users' AND column_name = 'profile_photo'
        """))
        
        if result.fetchone():
            print("✅ profile_photo column already exists in users table")
            return
        
        # Add the column
        print("📝 Adding profile_photo column to users table...")
        connection.execute(text("""
            ALTER TABLE users 
            ADD COLUMN profile_photo TEXT
        """))
        
        connection.commit()
        print("✅ profile_photo column added successfully!")

if __name__ == "__main__":
    try:
        add_profile_photo_column()
    except Exception as e:
        print(f"❌ Error adding profile_photo column: {e}")
        sys.exit(1)
