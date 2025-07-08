#!/usr/bin/env python3
"""
GitHub Upload Helper Script
Prepares and uploads the Base64 Image Converter to GitHub
"""

import os
import subprocess
import sys

def run_command(cmd, description, check=True):
    """Run a command and return success status."""
    print(f"\n🔧 {description}...")
    print(f"   Command: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
        if result.stdout:
            print(f"   Output: {result.stdout.strip()}")
        print(f"   ✅ Success!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Failed: {e}")
        if e.stderr:
            print(f"   Error details: {e.stderr}")
        return False

def main():
    """Main upload preparation function."""
    print("=" * 70)
    print("    BASE64 IMAGE CONVERTER - GITHUB UPLOAD HELPER")
    print("=" * 70)
    print()
    print("🚀 Repository: https://github.com/KCoderVA/Base64_ImageConverter")
    print()
    
    # Check if we're in the right directory
    if not os.path.exists('setup.py') or not os.path.exists('base64_image_converter'):
        print("❌ Error: This doesn't appear to be the Base64 Image Converter project directory.")
        input("Press Enter to exit...")
        sys.exit(1)
    
    print("✅ Project files found!")
    
    # Check Git status
    print("\n📋 Checking Git status...")
    run_command("git status --porcelain", "Checking for uncommitted changes", check=False)
    
    # Check if remote exists
    print("\n🔗 Checking Git remote configuration...")
    if not run_command("git remote get-url origin", "Checking origin remote", check=False):
        print("   Adding GitHub remote...")
        if run_command("git remote add origin https://github.com/KCoderVA/Base64_ImageConverter.git", "Adding origin remote"):
            print("   ✅ Remote added successfully!")
    else:
        print("   ✅ Remote already configured!")
    
    # Show current remotes
    run_command("git remote -v", "Showing configured remotes", check=False)
    
    print("\n" + "=" * 70)
    print("🎯 READY FOR GITHUB UPLOAD!")
    print("=" * 70)
    print()
    print("Next steps:")
    print("1. Review the files with: git status")
    print("2. Stage all files: git add .")
    print("3. Commit: git commit -m \"Initial release: Base64 Image Converter v1.0.0\"")
    print("4. Push to GitHub: git push -u origin main")
    print("5. Create a release on GitHub with the dist/ files")
    print()
    print("🔗 Repository URL: https://github.com/KCoderVA/Base64_ImageConverter")
    print()
    
    # Ask if user wants to proceed with upload
    response = input("Do you want to proceed with the upload now? (y/N): ").strip().lower()
    
    if response in ['y', 'yes']:
        print("\n🚀 Starting upload process...")
        
        # Stage all files
        if run_command("git add .", "Staging all files"):
            # Create commit
            commit_msg = """Initial release: Base64 Image Converter v1.0.0

- Complete bidirectional image/base64 converter
- Web GUI with modern interface  
- Command-line interface with interactive dialogs
- Professional Python package with entry points
- Comprehensive documentation and build tools
- Zero external dependencies"""
            
            if run_command(f'git commit -m "{commit_msg}"', "Creating commit"):
                # Push to GitHub
                if run_command("git push -u origin main", "Pushing to GitHub"):
                    print("\n🎉 SUCCESS! Your project has been uploaded to GitHub!")
                    print("🔗 Visit: https://github.com/KCoderVA/Base64_ImageConverter")
                    print("📦 Don't forget to create a release and upload the dist/ files!")
                else:
                    print("\n⚠️  Upload failed. You may need to resolve conflicts or check credentials.")
            else:
                print("\n⚠️  Commit failed. Check for issues or conflicts.")
        else:
            print("\n⚠️  Staging failed. Check for file issues.")
    else:
        print("\n📝 Upload cancelled. Use the commands above when you're ready!")
    
    print("\n" + "=" * 70)
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
