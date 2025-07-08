#!/usr/bin/env python3
"""
=====================================================================================
                    BIDIRECTIONAL BASE64 IMAGE CONVERTER UTILITY
=====================================================================================

Project:        Employee Recognition App - Image Processing Suite
Description:    Bidirectional converter: Images ↔ Base64 HTML format for web embedding
Version:        1.0.0
Author:         Data Team - Informatics Developer
Organization:   Healthcare Organization
Department:     Data Team - Informatics
Created:        July 8, 2025
Last Modified:  July 8, 2025

PURPOSE:
--------
This script provides bidirectional conversion between image files and base64-encoded 
HTML format. It can convert images (PNG, JPEG, GIF, BMP) to base64-embedded HTML 
structure AND reverse the process by extracting base64 data from HTML/text files 
to recreate the original image files. Perfect for web applications, emails, or any 
HTML document where you need to eliminate external image dependencies or recover 
images from base64-encoded sources.

FEATURES:
---------
• Bidirectional conversion: Image → Base64 HTML AND Base64 HTML → Image
• Automatic batch processing of mixed file types from input directory
• Interactive file/folder selection with GUI dialogs
• Comprehensive image format support (PNG, JPEG, GIF, BMP)
• Automatic dimension extraction from image headers
• Human-readable file size reporting
• HTML5-compliant output with proper metadata
• Detailed conversion information in HTML comments
• Smart file type detection and automatic conversion mode selection

DIRECTORY STRUCTURE:
-------------------
base64 Image Converter/
├── convertIMAGE_script.py     # This script
├── Inputs/                    # Default input directory (auto-scanned)
└── Outputs/                   # Default output directory

USAGE:
------
1. Place files in the 'Inputs' folder for automatic batch processing:
   • Image files (PNG, JPEG, GIF, BMP) → Convert to Base64 HTML
   • Text files containing Base64 HTML → Convert back to original images
2. OR run the script and select individual files via file dialog
3. Choose output directory (defaults to 'Outputs' folder)
4. Files are automatically converted to their opposite format

CONVERSION MODES:
-----------------
• Image → Base64: Creates .txt files with complete HTML and embedded base64
• Base64 → Image: Extracts base64 data from .txt files and recreates original images

OUTPUT FORMAT:
--------------
Image → Base64 conversion produces .txt files containing:
• Complete HTML5 document structure
• Detailed conversion metadata in HTML comments
• Optimized <img> tag with proper attributes
• Base64-encoded image data

Base64 → Image conversion produces:
• Original image files with proper extensions (.png, .jpg, .gif, .bmp)
• Reconstructed from embedded base64 data
• Maintains original image quality and format

DEPENDENCIES:
-------------
• Python 3.6+ (standard library only)
• tkinter (usually included with Python)

LICENSE:
--------
MIT License

Copyright (c) 2025 Data Team - Informatics

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

CHANGELOG:
----------
v1.0.0 (July 8, 2025)
  • Initial release with bidirectional base64 image conversion
  • Support for PNG, JPEG, GIF, and BMP formats
  • Automatic dimension extraction from image headers
  • Batch processing and interactive file selection modes
  • Professional HTML5 output with embedded metadata
  • Reverse conversion: Base64 HTML → Original image files
  • Intelligent file type detection and processing
  • Enhanced error handling and user feedback

CONTACT:
--------
For questions, bug reports, or feature requests, please contact:
Data Team - Informatics Department
Employee Recognition App Development Team

=====================================================================================
"""

import base64
import os
import mimetypes
import re
import tkinter as tk
from tkinter import filedialog

# =============================================================================
# CONFIGURATION CONSTANTS
# =============================================================================

# Get the directory where the script is located for relative path resolution
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set default input/output directories relative to script location
default_input_dir = os.path.join(script_dir, "Inputs")
default_output_dir = os.path.join(script_dir, "Outputs")

# Supported image file extensions for processing
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

# Supported text file extensions that may contain base64 data
text_extensions = ('.txt', '.html', '.htm')


# =============================================================================
# IMAGE DIMENSION EXTRACTION FUNCTIONS
# =============================================================================

def try_read_dimensions_from_header(image_path, mime_type):
    """
    Extract image dimensions directly from file headers without loading the entire image.
    
    This function reads the binary header of image files to extract width and height
    information efficiently. It supports PNG, JPEG, GIF, and BMP formats using
    format-specific header parsing techniques.
    
    Args:
        image_path (str): Full path to the image file
        mime_type (str): MIME type of the image (e.g., 'image/png', 'image/jpeg')
    
    Returns:
        tuple: (width, height) as integers, or (None, None) if extraction fails
    
    Supported Formats:
        • PNG: Reads IHDR chunk for dimensions
        • JPEG: Parses SOF (Start of Frame) markers
        • GIF: Reads logical screen descriptor
        • BMP: Extracts from DIB header
    """
    try:
        with open(image_path, "rb") as f:
            # PNG format: Read IHDR chunk
            if mime_type == "image/png":
                f.read(8)  # Skip PNG signature (8 bytes)
                chunk = f.read(25)  # Read chunk length, type, and IHDR data
                if chunk[12:16] == b'IHDR':  # Verify IHDR chunk type
                    width = int.from_bytes(chunk[16:20], "big")
                    height = int.from_bytes(chunk[20:24], "big")
                    return width, height
            
            # JPEG format: Parse markers to find SOF (Start of Frame)
            elif mime_type == "image/jpeg":
                f.read(2)  # Skip JPEG signature (FF D8)
                while True:
                    marker, code = f.read(1), f.read(1)
                    if marker != b'\xFF':
                        break
                    # Skip any additional 0xFF bytes
                    while code == b'\xFF':
                        code = f.read(1)
                    # Check for SOF markers (Start of Frame)
                    if 0xC0 <= code[0] <= 0xCF and code[0] != 0xC4 and code[0] != 0xCC:
                        f.read(3)  # Skip segment length and precision
                        height = int.from_bytes(f.read(2), "big")
                        width = int.from_bytes(f.read(2), "big")
                        return width, height
                    else:
                        # Skip to next marker
                        size = int.from_bytes(f.read(2), "big")
                        f.read(size-2)
            
            # GIF format: Read logical screen descriptor
            elif mime_type == "image/gif":
                header = f.read(10)  # Read GIF header (6 bytes signature + 4 bytes dimensions)
                width = int.from_bytes(header[6:8], "little")
                height = int.from_bytes(header[8:10], "little")
                return width, height
            
            # BMP format: Read DIB header
            elif mime_type == "image/bmp":
                f.read(18)  # Skip BMP file header and DIB header size
                width = int.from_bytes(f.read(4), "little")
                height = int.from_bytes(f.read(4), "little")
                return width, height
                
    except Exception:
        # Return None values if any error occurs during header parsing
        pass
    return None, None


# =============================================================================
# FILE UTILITY FUNCTIONS
# =============================================================================

def file_size_str(file_path):
    """
    Convert file size in bytes to human-readable format.
    
    Takes a file path and returns the file size formatted in appropriate units
    (bytes, KB, MB, GB, TB, PB) with 2 decimal places for readability.
    
    Args:
        file_path (str): Full path to the file
    
    Returns:
        str: Formatted file size string (e.g., "1.25 MB", "500 bytes")
    """
    try:
        size_bytes = os.path.getsize(file_path)
        
        # Convert bytes to human-readable format
        for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} PB"  # Fallback for extremely large files
        
    except Exception:
        return "Unknown"


# =============================================================================
# CORE IMAGE PROCESSING FUNCTION
# =============================================================================

def process_image(image_path, output_dir):
    """
    Convert a single image file to base64-encoded HTML format.
    
    This is the main processing function that handles the complete conversion workflow:
    1. Reads the source image file
    2. Encodes it as base64
    3. Extracts metadata and dimensions
    4. Generates a complete HTML document with embedded image
    5. Saves the result as a .txt file
    
    Args:
        image_path (str): Full path to the source image file
        output_dir (str): Directory where the output .txt file will be saved
    
    Output File Contents:
        • Complete HTML5 document
        • Detailed conversion metadata in HTML comments
        • Optimized <img> tag with proper attributes
        • Base64-encoded image data
    """
    # Extract filename components for processing
    filename = os.path.basename(image_path)
    base_name, ext = os.path.splitext(filename)
    output_filename = f"{base_name}.txt"
    output_path = os.path.join(output_dir, output_filename)

    # Determine MIME type based on file extension
    mime_type, _ = mimetypes.guess_type(filename)
    if not mime_type:
        mime_type = "image/png"  # Default to PNG if MIME type cannot be determined

    # Read image file and encode as Base64
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
        b64_string = base64.b64encode(img_bytes).decode('utf-8')

    # Attempt to extract image dimensions from file header
    img_width, img_height = try_read_dimensions_from_header(image_path, mime_type)

    # Prepare metadata for output documentation
    display_file_type = ext.lstrip(".").lower() if ext else "png"
    alt_str = f"{base_name}.{display_file_type}"
    image_file_size = file_size_str(image_path)
    b64_file_size = f"{len(b64_string.encode('utf-8')):.2f} bytes"
    b64_string_length = len(b64_string)

    # Generate dimension information blocks (conditional on successful extraction)
    dimensions_block = ""
    img_size_info = ""
    if img_width is not None and img_height is not None:
        dimensions_block = f"""\n               Image file dimensions:
                    Height: {img_height}
                    Width: {img_width}"""
        img_size_info = f'\n        width="{img_width}"\n        height="{img_height}"'

    # Generate complete HTML document with embedded base64 image
    output_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{filename}</title>
</head>
<body>

    <!-- 
    Source image file has been encoded/converted into a base64 format ready for HTML embedding, with the following conversion information:
        INPUT (source) image file details:     
            Image file name: {filename}
            Image file type: {mime_type}
            Image file size: {image_file_size}
            Image file location: {image_path}{dimensions_block}
        OUTPUT Encoded Base64 file:
            Base64 file name: {output_filename}
            Base64 file type: text/plain
            Base64 file location: {output_path}
            Base64 file size: {b64_file_size}
            Base64 individual string length: {b64_string_length}
    -->
    
    <img 
        src="data:{mime_type};base64,{b64_string}" 
        alt="{alt_str}" 
        class="{mime_type}"
        loading="lazy"
        decoding="async"{img_size_info}
    />

</body>
</html>
"""

    # Write the generated HTML content to output file
    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write(output_content)

    # Provide user feedback on successful conversion
    print(f"Converted '{filename}' to Base64 and saved as '{output_path}'")


# =============================================================================
# REVERSE CONVERSION FUNCTION (BASE64 → IMAGE)
# =============================================================================

def process_base64_file(text_file_path, output_dir):
    """
    Convert a base64-encoded HTML/text file back to its original image format.
    
    This function handles the reverse conversion workflow:
    1. Reads the text/HTML file containing base64 data
    2. Extracts the base64 string and MIME type information
    3. Decodes the base64 data back to binary image data
    4. Determines the appropriate file extension
    5. Saves the reconstructed image file
    
    Args:
        text_file_path (str): Full path to the source text/HTML file
        output_dir (str): Directory where the output image file will be saved
    
    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        # Read the content of the text file
        with open(text_file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Extract base64 data using regex pattern matching
        # Pattern to match data URI with base64 content
        pattern = r'data:([^;]+);base64,([A-Za-z0-9+/=]+)'
        match = re.search(pattern, content)
        
        if not match:
            print(f"❌ No valid base64 data found in '{os.path.basename(text_file_path)}'")
            return False
        
        # Extract MIME type and base64 string
        mime_type = match.group(1)
        b64_string = match.group(2)
        
        # Determine file extension from MIME type
        extension_map = {
            'image/png': '.png',
            'image/jpeg': '.jpg',
            'image/jpg': '.jpg',
            'image/gif': '.gif',
            'image/bmp': '.bmp'
        }
        
        file_extension = extension_map.get(mime_type, '.png')  # Default to PNG
        
        # Generate output filename
        base_name = os.path.splitext(os.path.basename(text_file_path))[0]
        output_filename = f"{base_name}{file_extension}"
        output_path = os.path.join(output_dir, output_filename)
        
        # Decode base64 data to binary
        try:
            img_bytes = base64.b64decode(b64_string)
        except Exception as e:
            print(f"❌ Failed to decode base64 data in '{os.path.basename(text_file_path)}': {e}")
            return False
        
        # Write binary data to image file
        with open(output_path, "wb") as img_file:
            img_file.write(img_bytes)
        
        # Calculate file sizes for reporting
        original_size = file_size_str(text_file_path)
        new_size = file_size_str(output_path)
        
        # Provide user feedback
        print(f"✓ Decoded '{os.path.basename(text_file_path)}' → '{output_filename}' ({mime_type}, {new_size})")
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing '{os.path.basename(text_file_path)}': {e}")
        return False


# =============================================================================
# UNIFIED FILE PROCESSING FUNCTION
# =============================================================================

def process_file(file_path, output_dir):
    """
    Intelligently process a file based on its type - either convert image to base64 
    or convert base64 back to image.
    
    Args:
        file_path (str): Full path to the source file
        output_dir (str): Directory where the output file will be saved
    
    Returns:
        bool: True if conversion successful, False otherwise
    """
    filename = os.path.basename(file_path)
    file_ext = os.path.splitext(filename)[1].lower()
    
    if file_ext in image_extensions:
        # Convert image to base64 HTML
        try:
            process_image(file_path, output_dir)
            return True
        except Exception as e:
            print(f"❌ Failed to convert image '{filename}': {e}")
            return False
    
    elif file_ext in text_extensions:
        # Convert base64 HTML back to image
        return process_base64_file(file_path, output_dir)
    
    else:
        print(f"⚠️  Unsupported file type: '{filename}' (skipping)")
        return False


# =============================================================================
# USER INTERFACE FUNCTIONS
# =============================================================================

def select_input_file(initial_dir):
    """
    Open a file dialog for user to select an input file (image or text with base64).
    
    Creates a GUI file picker dialog allowing users to browse and select
    files for conversion. The dialog accepts both image files and text files
    containing base64 data, providing bidirectional conversion capability.
    
    Args:
        initial_dir (str): Directory to open in the file dialog by default
    
    Returns:
        str: Full path to selected file, or empty string if cancelled
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    
    file_path = filedialog.askopenfilename(
        title="Select a file for conversion (Image → Base64 or Base64 → Image)",
        initialdir=initial_dir,
        filetypes=[
            ("All supported files", "*.png *.jpg *.jpeg *.gif *.bmp *.txt *.html *.htm"),
            ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"), 
            ("Text files", "*.txt *.html *.htm"),
            ("All files", "*.*")
        ]
    )
    
    root.destroy()  # Clean up tkinter resources
    return file_path


def select_output_directory(initial_dir):
    """
    Open a directory dialog for user to select output folder.
    
    Creates a GUI folder picker dialog allowing users to choose where
    the converted base64 .txt files will be saved.
    
    Args:
        initial_dir (str): Directory to open in the dialog by default
    
    Returns:
        str: Full path to selected directory, or empty string if cancelled
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    
    folder_selected = filedialog.askdirectory(
        title="Select Output Folder for Base64 .txt Files",
        initialdir=initial_dir
    )
    
    root.destroy()  # Clean up tkinter resources
    return folder_selected


# =============================================================================
# MAIN EXECUTION LOGIC
# =============================================================================

def main():
    """
    Main execution function that orchestrates the bidirectional conversion workflow.
    
    This function implements the complete conversion process:
    1. Scans default input directory for files (batch mode)
    2. Falls back to file dialog if no files found (interactive mode)  
    3. Prompts user for output directory selection
    4. Intelligently processes all selected files based on their type
    5. Provides detailed user feedback throughout the process
    
    Processing Modes:
        • Batch Mode: Automatically processes all files in 'Inputs' folder
        • Interactive Mode: User selects individual file via file dialog
    
    Conversion Types:
        • Image files → Base64 HTML text files
        • Text files with Base64 → Original image files
    """
    print("=" * 80)
    print("          BIDIRECTIONAL BASE64 IMAGE CONVERTER UTILITY")
    print("=" * 80)
    print("Converting files between image and base64-encoded HTML formats...")
    print()

    # Step 1: Search for convertible files in the default input directory
    if os.path.isdir(default_input_dir):
        all_files = os.listdir(default_input_dir)
        
        # Find image files for encoding
        found_images = [
            os.path.join(default_input_dir, f)
            for f in all_files
            if f.lower().endswith(image_extensions)
        ]
        
        # Find text files for potential decoding
        found_text_files = [
            os.path.join(default_input_dir, f)
            for f in all_files
            if f.lower().endswith(text_extensions)
        ]
        
        # Combine all convertible files
        found_files = found_images + found_text_files
    else:
        found_files = []

    # Determine processing mode based on found files
    if found_files:
        # Batch Mode: Process all files found in input directory
        selected_files = found_files
        print(f"BATCH MODE: Found {len(selected_files)} convertible file(s) in the input folder:")
        
        # Categorize and display found files
        image_count = len(found_images)
        text_count = len(found_text_files)
        
        if image_count > 0:
            print(f"  • {image_count} image file(s) → will convert to Base64 HTML")
        if text_count > 0:
            print(f"  • {text_count} text file(s) → will attempt Base64 → Image conversion")
            
        print("Proceeding with automatic batch conversion...")
        print()
    else:
        # Interactive Mode: Prompt user to select individual file
        print("INTERACTIVE MODE: No convertible files found in the input folder.")
        print("Please select a file using the file picker dialog.")
        print("(Supports: Images → Base64 HTML, or Text files with Base64 → Images)")
        print()
        
        selected_file = select_input_file(default_input_dir)
        if selected_file:
            selected_files = [selected_file]
            print(f"Selected: {os.path.basename(selected_file)}")
            print()
        else:
            print("No source file selected. Exiting program.")
            return

    # Step 2: Get output directory from user (with fallback to default)
    print("Please select the output folder where converted files will be saved.")
    output_dir = select_output_directory(default_output_dir)
    
    if not output_dir:
        output_dir = default_output_dir
        print(f"No output folder selected. Using default: {default_output_dir}")
    else:
        print(f"Output directory: {output_dir}")
    
    print()

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Step 3: Process all selected files with intelligent conversion
    print("Processing files...")
    print("-" * 70)
    
    successful_conversions = 0
    failed_conversions = 0
    
    for i, file_path in enumerate(selected_files, 1):
        filename = os.path.basename(file_path)
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Determine conversion direction
        if file_ext in image_extensions:
            conversion_type = "Image → Base64 HTML"
        elif file_ext in text_extensions:
            conversion_type = "Base64 HTML → Image"
        else:
            conversion_type = "Unknown"
        
        print(f"[{i}/{len(selected_files)}] {conversion_type}: {filename}")
        
        # Process the file
        success = process_file(file_path, output_dir)
        if success:
            successful_conversions += 1
        else:
            failed_conversions += 1
        
        print()  # Add spacing between files
    
    # Final summary
    print("-" * 70)
    print("CONVERSION SUMMARY:")
    print(f"✓ Successfully converted: {successful_conversions} file(s)")
    if failed_conversions > 0:
        print(f"❌ Failed conversions: {failed_conversions} file(s)")
    print(f"📁 Output location: {output_dir}")
    print()
    
    if successful_conversions > 0:
        print("🎉 Conversion process completed successfully!")
    else:
        print("⚠️  No files were successfully converted.")


# =============================================================================
# SCRIPT ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    # Execute main function when script is run directly
    main()