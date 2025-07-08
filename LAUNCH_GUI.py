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

Contact Information:
- Author: Kyle J. Coder
- Organization: Advanced Analytics & Informatics, Edward Hines Jr. VA Hospital (v12/578), Veterans Health Administration, Department of Veterans Affairs
- Professional Email: HinClinicalAnalytics@va.gov

Double-Click GUI Launcher for Base64 Image Converter

This script provides a simple way for users to launch the web interface
by double-clicking this file in their file explorer.
"""

import os
import sys
import subprocess
import time

def main():
    """Launch the GUI interface"""
    print("🚀 Starting Base64 Image Converter...")
    print("=" * 50)
    
    # Change to the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Add the project directory to Python path
    project_path = os.path.join(script_dir, 'project')
    if project_path not in sys.path:
        sys.path.insert(0, project_path)
    
    try:
        # Try to launch using the installed console command first
        print("🔧 Attempting to launch via console command...")
        result = subprocess.run(["base64-converter-gui"], 
                              capture_output=True, text=True, timeout=5)
        
        if result.returncode != 0:
            # Fallback to module execution from project directory
            print("🔧 Fallback: Launching via module...")
            subprocess.run([sys.executable, "-m", "base64_image_converter.launch_gui"], 
                         cwd=project_path)
        
    except (subprocess.TimeoutExpired, FileNotFoundError):
        # If console command doesn't work, try direct module execution
        print("🔧 Launching directly from project directory...")
        try:
            subprocess.run([sys.executable, "-m", "base64_image_converter.launch_gui"], 
                         cwd=project_path)
        except Exception as e:
            print(f"❌ Error launching GUI: {e}")
            print("\n💡 Please try running 'python SETUP.py' first")
            print("📁 Make sure the project/ folder exists with the package files")
            input("Press Enter to exit...")
            return

if __name__ == "__main__":
    main()
