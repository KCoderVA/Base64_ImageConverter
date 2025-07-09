#!/usr/bin/env python3
"""
Base64 Image Converter Package
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

__version__ = "1.0.1"
__author__ = "Kyle J. Coder"
__email__ = "HinClinicalAnalytics@va.gov"
__license__ = "AGPL-3.0"
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
