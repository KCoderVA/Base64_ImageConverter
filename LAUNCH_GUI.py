#!/usr/bin/env python3
"""
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
