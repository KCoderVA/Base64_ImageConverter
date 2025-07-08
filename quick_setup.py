#!/usr/bin/env python3
"""
Simple setup script to prepare the Base64 Image Converter for use.

This script ensures all dependencies are installed and the project is ready to run.
"""

import os
import sys
import subprocess

def run_command(cmd, description):
    """Run a command and return success status."""
    print(f"\n🔧 {description}...")
    print(f"   Command: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"   ✅ Success!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Failed: {e}")
        if e.stderr:
            print(f"   Error details: {e.stderr}")
        return False

def main():
    """Main setup function."""
    print("=" * 60)
    print("  BASE64 IMAGE CONVERTER - QUICK SETUP")
    print("=" * 60)
    print()
    print("This script will prepare your environment for the Base64 Image Converter.")
    print()
    
    # Check if we're in the right directory
    if not os.path.exists('setup.py') or not os.path.exists('base64_image_converter'):
        print("❌ Error: This doesn't appear to be the Base64 Image Converter project directory.")
        print("   Please run this script from the project root directory.")
        print("   Looking for: setup.py and base64_image_converter/ folder")
        input("Press Enter to exit...")
        sys.exit(1)
    
    print("✅ Project files found!")
    
    # Install basic requirements
    print("\n📦 Installing/upgrading build tools...")
    
    commands = [
        ("py -m pip install --upgrade pip", "Upgrading pip"),
        ("py -m pip install --upgrade setuptools", "Installing setuptools"),
        ("py -m pip install --upgrade wheel", "Installing wheel"),
    ]
    
    success_count = 0
    for cmd, desc in commands:
        if run_command(cmd, desc):
            success_count += 1
    
    # Install the package in development mode
    if success_count >= 2:
        print("\n📦 Installing Base64 Image Converter package...")
        if run_command("py -m pip install -e .", "Installing package in development mode"):
            success_count += 1
            package_installed = True
        else:
            package_installed = False
    else:
        package_installed = False
    
    print(f"\n📊 Setup Results: {success_count}/{len(commands) + (1 if success_count >= 2 else 0)} successful")
    
    if package_installed:
        print("\n🎉 Complete setup successful!")
        print("\nYou can now use the Base64 Image Converter:")
        print("   • base64-converter-gui       # Launch web interface")
        print("   • base64-converter           # Command line interface") 
        print("   • base64-converter-web       # Direct web server")
        print("\nOr run modules directly:")
        print("   • python -m base64_image_converter.launch_gui")
        print("   • python -m base64_image_converter.convertIMAGE_script")
    elif success_count >= 2:  # At least pip and one other tool
        print("\n✅ Environment setup complete!")
        print("\nYou can now:")
        print("   • Install package: pip install -e .")
        print("   • Run the GUI: python -m base64_image_converter.launch_gui")
        print("   • Run command line: python -m base64_image_converter.convertIMAGE_script")
        print("   • Build package: python build_and_test.py")
        print("\nFor easier use after installation:")
        print("   • base64-converter-gui       # Launch web interface")
        print("   • base64-converter           # Command line interface")
        print("   • base64-converter-web       # Direct web server")
    else:
        print("\n⚠️  Some dependencies failed to install.")
        print("The converter might still work with basic functionality.")
    
    print("\n" + "=" * 60)
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
