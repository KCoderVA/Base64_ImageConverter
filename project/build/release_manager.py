#!/usr/bin/env python3
"""
Base64 Image Converter - Convert images to Base64 and vice versa
Copyright (C) 2025 Kyle J. Coder
Advanced Analytics & Informatics, Edward Hines Jr. VA Hospital (v12/578)
Veterans Health Administration, Department of Veterans Affairs

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

Contact: HinClinicalAnalytics@va.gov

Version management and release preparation script.
"""

import os
import sys
import subprocess
import re
from datetime import datetime

def get_current_version():
    """Read current version from __init__.py"""
    init_file = "project/base64_image_converter/__init__.py"
    with open(init_file, 'r') as f:
        content = f.read()
        match = re.search(r'__version__ = "([^"]+)"', content)
        return match.group(1) if match else "unknown"

def update_version_files(new_version):
    """Update version in all relevant files"""
    files_to_update = [
        ("project/base64_image_converter/__init__.py", r'__version__ = "[^"]+"', f'__version__ = "{new_version}"'),
        ("project/setup.py", r'version="[^"]+"', f'version="{new_version}"'),
    ]
    
    for file_path, pattern, replacement in files_to_update:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            
            updated_content = re.sub(pattern, replacement, content)
            
            with open(file_path, 'w') as f:
                f.write(updated_content)
            
            print(f"✅ Updated version in {file_path}")

def main():
    """Main release preparation function"""
    print("🚀 Base64 Image Converter - Release Manager")
    print("=" * 50)
    
    current_version = get_current_version()
    print(f"Current version: {current_version}")
    
    print("\nAvailable actions:")
    print("1. Check current status")
    print("2. Update version number")
    print("3. Create git tag")
    print("4. Exit")
    
    choice = input("\nSelect an action (1-4): ").strip()
    
    if choice == "1":
        # Show git status
        print("\n📊 Git Status:")
        subprocess.run(["git", "status", "--short"])
        
        print(f"\n📋 Current Version: {current_version}")
        print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d')}")
        
    elif choice == "2":
        new_version = input(f"Enter new version (current: {current_version}): ").strip()
        if new_version and new_version != current_version:
            update_version_files(new_version)
            print(f"✅ Version updated to {new_version}")
        else:
            print("❌ Invalid or same version")
            
    elif choice == "3":
        tag_name = input("Enter tag name (e.g., v1.0.1): ").strip()
        message = input("Enter tag message: ").strip()
        
        if tag_name and message:
            try:
                subprocess.run(["git", "tag", "-a", tag_name, "-m", message], check=True)
                print(f"✅ Created tag: {tag_name}")
                print("💡 Don't forget to push tags: git push origin --tags")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to create tag: {e}")
        else:
            print("❌ Tag name and message are required")
            
    elif choice == "4":
        print("👋 Goodbye!")
        return
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
