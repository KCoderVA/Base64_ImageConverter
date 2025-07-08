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
    
    # Change to the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    try:
        # Try to launch using the installed console command first
        print("🔧 Attempting to launch via console command...")
        result = subprocess.run(["base64-converter-gui"], 
                              capture_output=True, text=True, timeout=5)
        
        if result.returncode != 0:
            # Fallback to module execution
            print("🔧 Fallback: Launching via module...")
            subprocess.run([sys.executable, "-m", "base64_image_converter.launch_gui"])
        
    except (subprocess.TimeoutExpired, FileNotFoundError):
        # If console command doesn't work, try direct module execution
        print("🔧 Launching directly...")
        try:
            subprocess.run([sys.executable, "-m", "base64_image_converter.launch_gui"])
        except Exception as e:
            print(f"❌ Error launching GUI: {e}")
            print("\n💡 Please try running 'python quick_setup.py' first")
            input("Press Enter to exit...")
            return

if __name__ == "__main__":
    main()
