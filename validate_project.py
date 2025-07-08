#!/usr/bin/env python3
"""
Final Project Validation Script

This script validates that the Base64 Image Converter project is properly
configured and ready for GitHub publication.
"""

import os
import sys
import subprocess
from pathlib import Path

def validate_file_structure():
    """Validate that all required files are present"""
    print("🔍 Validating project structure...")
    
    required_files = [
        'README.md',
        'CHANGELOG.md',
        'CONTRIBUTING.md',
        'LICENSE',
        'setup.py',
        'pyproject.toml',
        'requirements.txt',
        'MANIFEST.in',
        '.gitignore',
        'build_and_test.py',
        'quick_setup.py',
        'PROJECT_STATUS.md',
        'base64_image_converter/__init__.py',
        'base64_image_converter/convertIMAGE_script.py',
        'base64_image_converter/Base64_Converter_GUI.html',
        'base64_image_converter/web_bridge.py',
        'base64_image_converter/launch_gui.py',
        'Inputs/.gitkeep',
        'Outputs/.gitkeep',
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   • {file}")
        return False
    else:
        print("✅ All required files present")
        return True

def validate_package_imports():
    """Test that the package can be imported correctly"""
    print("\n🔍 Validating package imports...")
    
    try:
        # Test basic package import
        import base64_image_converter
        print("✅ Package imports successfully")
        
        # Test version information
        if hasattr(base64_image_converter, '__version__'):
            print(f"✅ Package version: {base64_image_converter.__version__}")
        else:
            print("⚠️  Package version not found")
            
        return True
    except ImportError as e:
        print(f"❌ Package import failed: {e}")
        return False

def validate_console_scripts():
    """Check that console scripts are properly configured"""
    print("\n🔍 Validating console script configuration...")
    
    # Check setup.py for entry points
    try:
        with open('setup.py', 'r') as f:
            setup_content = f.read()
            
        if 'entry_points' in setup_content:
            print("✅ Entry points found in setup.py")
            if 'base64-converter=' in setup_content:
                print("✅ base64-converter entry point configured")
            if 'base64-converter-gui=' in setup_content:
                print("✅ base64-converter-gui entry point configured")
            if 'base64-converter-web=' in setup_content:
                print("✅ base64-converter-web entry point configured")
            return True
        else:
            print("❌ No entry points found in setup.py")
            return False
    except Exception as e:
        print(f"❌ Error reading setup.py: {e}")
        return False

def validate_documentation():
    """Check that documentation files have content"""
    print("\n🔍 Validating documentation...")
    
    doc_files = {
        'README.md': 1000,  # Minimum expected length
        'CHANGELOG.md': 500,
        'CONTRIBUTING.md': 200,
        'PROJECT_STATUS.md': 1000,
    }
    
    all_valid = True
    for doc_file, min_length in doc_files.items():
        try:
            with open(doc_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if len(content) >= min_length:
                print(f"✅ {doc_file} ({len(content)} chars)")
            else:
                print(f"⚠️  {doc_file} seems too short ({len(content)} chars)")
                all_valid = False
        except Exception as e:
            print(f"❌ Error reading {doc_file}: {e}")
            all_valid = False
    
    return all_valid

def validate_distributions():
    """Check if distribution files exist"""
    print("\n🔍 Validating distribution files...")
    
    dist_dir = Path('dist')
    if not dist_dir.exists():
        print("⚠️  No dist directory found - run build_and_test.py first")
        return False
    
    wheel_files = list(dist_dir.glob('*.whl'))
    source_files = list(dist_dir.glob('*.tar.gz'))
    
    if wheel_files:
        print(f"✅ Wheel distribution found: {wheel_files[0].name}")
    else:
        print("⚠️  No wheel distribution found")
    
    if source_files:
        print(f"✅ Source distribution found: {source_files[0].name}")
    else:
        print("⚠️  No source distribution found")
    
    return bool(wheel_files or source_files)

def main():
    """Main validation function"""
    print("=" * 60)
    print("  BASE64 IMAGE CONVERTER - PROJECT VALIDATION")
    print("=" * 60)
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    tests = [
        validate_file_structure,
        validate_package_imports,
        validate_console_scripts,
        validate_documentation,
        validate_distributions,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            results.append(False)
    
    # Summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"🎉 ALL TESTS PASSED ({passed}/{total})")
        print("✅ Project is ready for GitHub publication!")
        return 0
    else:
        print(f"⚠️  {passed}/{total} tests passed")
        print("❌ Please address the issues above before publication")
        return 1

if __name__ == "__main__":
    sys.exit(main())
