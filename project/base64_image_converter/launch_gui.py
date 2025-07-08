#!/usr/bin/env python3
"""
=====================================================================================
                    LAUNCH BASE64 CONVERTER WEB INTERFACE
=====================================================================================

Simple launcher script to start the web-based GUI for the Base64 Image Converter.

Usage:
    Double-click this file or run: python launch_gui.py

Requirements:
    - Part of the base64_image_converter package
    - Uses packaged resources for HTML and web components
"""

import os
import sys
import subprocess
import webbrowser
import time
import pkg_resources

def get_package_file_path(filename):
    """Get the path to a file within the package"""
    try:
        # Try to get the file from the package resources
        return pkg_resources.resource_filename('base64_image_converter', filename)
    except:
        # Fallback to current directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, filename)

def check_required_files():
    """Check if all required files are present"""
    required_files = [
        'convertIMAGE_script.py',
        'Base64_Converter_GUI.html',
        'web_bridge.py'
    ]
    
    missing_files = []
    for file in required_files:
        file_path = get_package_file_path(file)
        if not os.path.exists(file_path):
            missing_files.append(file)
    
    return missing_files

def main():
    print("=" * 80)
    print("          BASE64 IMAGE CONVERTER - GUI LAUNCHER")
    print("=" * 80)
    print()
    
    # Check for required files
    missing_files = check_required_files()
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   • {file}")
        print()
        print("Please make sure all files are in the same directory and try again.")
        input("Press Enter to exit...")
        return
    
    print("✅ All required files found!")
    print("🚀 Starting web interface...")
    print()
    
    try:
        # Start the web server using the package module
        print("📡 Launching web server...")
        web_bridge_path = get_package_file_path('web_bridge.py')
        subprocess.run([sys.executable, web_bridge_path])
        
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except FileNotFoundError:
        print("❌ Error: Python not found. Please make sure Python is installed.")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
