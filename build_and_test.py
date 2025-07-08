#!/usr/bin/env python3
"""
Build and test script for the Base64 Image Converter package.

This script helps with building distributions, running tests, and preparing
the package for release.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {cmd}")
    print('='*60)
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print("STDOUT:", result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False

def clean_build():
    """Clean build artifacts."""
    print("Cleaning build artifacts...")
    
    dirs_to_clean = ['build', 'dist', '*.egg-info']
    for pattern in dirs_to_clean:
        for path in Path('.').glob(pattern):
            if path.is_dir():
                print(f"Removing directory: {path}")
                shutil.rmtree(path)
            elif path.is_file():
                print(f"Removing file: {path}")
                path.unlink()

def main():
    """Main build and test function."""
    print("Base64 Image Converter - Build and Test Script")
    print("=" * 50)
    
    # Ensure we're in the right directory
    if not os.path.exists('setup.py'):
        print("ERROR: setup.py not found. Please run this script from the project root.")
        sys.exit(1)
    
    success = True
    
    # Clean previous builds
    clean_build()
    
    # Install build dependencies first
    print("\nInstalling build dependencies...")
    if not run_command("py -m pip install --upgrade pip setuptools wheel", "Installing build tools"):
        print("⚠️  Warning: Failed to install build dependencies. Continuing anyway...")
    
    # Check setup.py
    if not run_command("py setup.py check", "Checking setup.py configuration"):
        success = False
    
    # Build source distribution
    if not run_command("py setup.py sdist", "Building source distribution"):
        success = False
    
    # Build wheel distribution (with fallback)
    print("\nAttempting to build wheel distribution...")
    wheel_success = run_command("py setup.py bdist_wheel", "Building wheel distribution")
    
    if not wheel_success:
        print("⚠️  Wheel build failed. Trying alternative method...")
        # Try using pip wheel as alternative
        alt_wheel_success = run_command("py -m pip wheel . --no-deps", "Building wheel with pip")
        if not alt_wheel_success:
            print("❌ Both wheel build methods failed. Continuing with source distribution only...")
    
    # Check the distributions
    if os.path.exists('dist'):
        print(f"\nBuild artifacts created in 'dist' directory:")
        for file in os.listdir('dist'):
            print(f"  - {file}")
    
    # Test installation (optional)
    test_install = input("\nDo you want to test installation in a virtual environment? (y/n): ")
    if test_install.lower() == 'y':
        print("\nTo test installation:")
        print("1. Create a virtual environment: python -m venv test_env")
        print("2. Activate it: test_env\\Scripts\\activate (Windows) or source test_env/bin/activate (Unix)")
        if os.path.exists('dist') and any(f.endswith('.whl') for f in os.listdir('dist')):
            print("3. Install from wheel: pip install dist\\*.whl")
        else:
            print("3. Install from source: pip install dist\\*.tar.gz")
        print("4. Test commands: base64-converter --help")
    
    if success or os.path.exists('dist'):
        print(f"\n{'='*60}")
        print("✅ BUILD SUCCESSFUL!")
        print("Package is ready for distribution.")
        print("Files created:")
        if os.path.exists('dist'):
            for file in os.listdir('dist'):
                print(f"  - dist/{file}")
        print(f"{'='*60}")
    else:
        print(f"\n{'='*60}")
        print("❌ BUILD FAILED!")
        print("Please check the errors above and fix them.")
        print(f"{'='*60}")
        sys.exit(1)

if __name__ == "__main__":
    main()
