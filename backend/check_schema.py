#!/usr/bin/env python3
"""
Script to check the actual database schema for the users table.
"""

import sys
sys.path.append('.')

from sqlalchemy import text
from app.database import engine

def check_users_schema():
    """Check the schema of the users table."""
    
    with engine.connect() as connection:
        # Get all columns in the users table
        result = connection.execute(text("""
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns 
            WHERE table_name = 'users'
            ORDER BY ordinal_position
        """))
        
        columns = result.fetchall()
        
        print("📋 Users table schema:")
        print("-" * 50)
        for column in columns:
            print(f"  {column[0]:<20} {column[1]:<15} {column[2]}")
        
        # Check specifically for profile_photo
        profile_photo_exists = any(col[0] == 'profile_photo' for col in columns)
        print("-" * 50)
        if profile_photo_exists:
            print("✅ profile_photo column exists")
        else:
            print("❌ profile_photo column is missing")

if __name__ == "__main__":
    try:
        check_users_schema()
    except Exception as e:
        print(f"❌ Error checking schema: {e}")
        sys.exit(1)
