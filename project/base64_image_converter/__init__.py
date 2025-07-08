#!/usr/bin/env python3
"""
Base64 Image Converter Package

A comprehensive tool for bidirectional conversion between image files and 
base64-encoded HTML format. Perfect for web applications, emails, or any 
HTML document where you need to eliminate external image dependencies.

Features:
- Convert images (PNG, JPEG, GIF, BMP) to base64-embedded HTML
- Extract base64 data from HTML/text files to recreate original images
- Batch processing and interactive file selection
- Web-based GUI interface
- Command-line interface

Modules:
- convertIMAGE_script: Core conversion functionality
- web_bridge: Web server for GUI interface
- launch_gui: GUI launcher
"""

__version__ = "1.0.0"
__author__ = "Data Team - Informatics Developer"
__email__ = "informatics@healthcareorg.com"
__description__ = "Bidirectional converter for images and base64-encoded HTML format"

# Import main functions for easy access
try:
    from .convertIMAGE_script import main as convert_main, process_image, process_base64_file
    from .web_bridge import main as web_main
    from .launch_gui import main as gui_main
    
    __all__ = [
        'convert_main',
        'process_image', 
        'process_base64_file',
        'web_main',
        'gui_main',
    ]
except ImportError:
    # Handle case where modules might not be available during setup
    __all__ = []
