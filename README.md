# 🔄 Base64 Image Converter

A comprehensive, professional tool for bidirectional conversion between image files and base64-encoded HTML format. Perfect for web applications, emails, or any HTML document where you need to eliminate external image dependencies.

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Release](https://img.shields.io/github/v/release/KCoderVA/Base64_ImageConverter)](https://github.com/KCoderVA/Base64_ImageConverter/releases)
[![Package Status](https://img.shields.io/badge/Status-Production--Ready-green.svg)](https://github.com/KCoderVA/Base64_ImageConverter)

## ✨ Features

- **🔄 Bidirectional Conversion**: Images ↔ Base64 HTML format
- **📁 Batch Processing**: Process multiple files automatically
- **🌐 Web GUI**: Modern, responsive web interface
- **💻 Command Line**: Professional CLI with interactive dialogs
- **📦 Easy Installation**: Install via pip with console commands
- **🎨 Beautiful Interface**: Colorful, user-friendly design
- **🔧 Format Support**: PNG, JPEG, GIF, BMP image formats
- **📱 Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Installation

### Method 1: Install from GitHub (Recommended)

```bash
# Clone the repository
git clone https://github.com/KCoderVA/Base64_ImageConverter.git
cd Base64_ImageConverter

# Quick setup (installs dependencies and package)
python quick_setup.py
```

### Method 2: Install from Package

```bash
# Install from wheel distribution (if available)
pip install dist/base64_image_converter-1.0.0-py3-none-any.whl

# Or install from source distribution
pip install dist/base64_image_converter-1.0.0.tar.gz
```

### Method 3: Development Installation

```bash
# Clone the repository
git clone https://github.com/KCoderVA/Base64_ImageConverter.git
cd Base64_ImageConverter

# Install in development mode
pip install -e .
```

## 🎯 Usage Options

After installation, you have multiple ways to use the converter:

### 🖥️ Console Commands (Installed Globally)

```bash
# Interactive command-line interface
base64-converter

# Launch web-based GUI
base64-converter-gui

# Start web server directly
base64-converter-web
```

### 🌐 Web Interface

1. **Launch the GUI**:
   ```bash
   base64-converter-gui
   ```
   Or double-click `launch_gui.py`

2. **Open your browser** to `http://localhost:8080`

3. **Start converting**:
   - Drag & drop files onto the interface
   - Choose conversion mode (auto-detect recommended)
   - Download your converted files

### 💻 Command Line Interface

```bash
# Interactive mode with file dialogs
base64-converter

# Process files in the Inputs folder
# Place images or base64 text files in ./Inputs/
base64-converter
```

## 📁 Project Structure

```
base64-image-converter/
├── base64_image_converter/           # Main package
│   ├── __init__.py                   # Package initialization
│   ├── convertIMAGE_script.py        # Core conversion engine
│   ├── Base64_Converter_GUI.html     # Web interface
│   ├── web_bridge.py                 # Web server bridge
│   └── launch_gui.py                 # GUI launcher
├── Inputs/                           # Default input directory
├── Outputs/                          # Default output directory
├── dist/                             # Distribution packages
│   ├── base64_image_converter-1.0.0-py3-none-any.whl
│   └── base64_image_converter-1.0.0.tar.gz
├── setup.py                          # Package configuration
├── pyproject.toml                    # Build system config
├── requirements.txt                  # Dependencies
├── README.md                         # This file
├── LICENSE                           # MIT License
├── CHANGELOG.md                      # Version history
├── CONTRIBUTING.md                   # Contribution guidelines
├── build_and_test.py                 # Build automation
└── quick_setup.py                    # Dependency installer
```

## 🔄 Conversion Modes

### 📸 Images → Base64 HTML

**Input**: Image files (PNG, JPEG, GIF, BMP)  
**Output**: Text files with complete HTML5 documents containing embedded base64 images

**Example Output**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>example.png</title>
</head>
<body>
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..." 
         alt="example.png" 
         width="800" 
         height="600" />
</body>
</html>
```

### 📄 Base64 HTML → Images

**Input**: Text/HTML files containing base64 image data  
**Output**: Original image files with proper extensions

The converter automatically:
- Detects base64 data patterns in text files
- Extracts MIME type information
- Reconstructs original image files
- Maintains image quality and format

## 🎨 Web Interface Features

### 🏠 **Main Dashboard**
- **Modern Design**: Professional, colorful interface
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Intuitive Navigation**: Clear sections for tutorial, controls, and results

### 📚 **Tutorial Section**
- **Purpose Explanation**: Clear description of bidirectional conversion
- **Feature Overview**: Visual breakdown of capabilities
- **Quick Start Guide**: Step-by-step usage instructions
- **Conversion Examples**: Visual representation of workflows

### 🎛️ **Control Panel**
- **Drag & Drop Zone**: Simply drag files onto the interface
- **File Selection**: Browse for individual files or folders
- **Conversion Modes**:
  - 🔄 **Auto-Detect** (Recommended): Automatically determines conversion direction
  - 📸 → 📄 **Images to Base64**: Force image-to-HTML conversion
  - 📄 → 📸 **Base64 to Images**: Force HTML-to-image conversion
- **Progress Tracking**: Real-time progress bar and status indicators

### 📊 **Results Display**
- **Summary Cards**: Visual results for each converted file
- **Download Links**: Direct download buttons for converted files
- **Success/Error Tracking**: Clear indication of conversion status
- **File Information**: Shows original and output file details

### 📋 **Process Log**
- **Real-time Logging**: See exactly what's happening during conversion
- **Color-coded Messages**: Info (blue), Success (green), Warning (yellow), Error (red)
- **Timestamps**: Track when each operation occurred
- **Scrollable History**: Review the complete conversion process

## 🛠️ Technical Specifications

### **Requirements**
- **Python**: 3.6 or higher
- **Dependencies**: Standard library only (no external packages required)
- **Platform**: Windows, macOS, Linux
- **Browser**: Any modern web browser for GUI interface

### **Architecture**
- **Package Structure**: Professional Python package with proper entry points
- **Frontend**: HTML5, CSS3, JavaScript (runs in any modern browser)
- **Backend**: Python HTTP server with bidirectional conversion logic
- **Integration**: RESTful API communication between GUI and Python engine

### **Performance**
- **Memory Efficient**: Processes files one at a time
- **Fast Conversion**: Direct base64 encoding/decoding
- **Batch Processing**: Handles multiple files automatically
- **Error Handling**: Comprehensive error detection and reporting

## 📦 Building and Distribution

### **For Developers**

```bash
# Install build dependencies
python quick_setup.py

# Build distribution packages
python build_and_test.py

# Install in development mode
pip install -e .

# Test installation
base64-converter --help
```

### **Build Outputs**
- **Wheel Package**: `dist/base64_image_converter-1.0.0-py3-none-any.whl`
- **Source Distribution**: `dist/base64_image_converter-1.0.0.tar.gz`

### **Console Scripts**
After installation, these commands are available globally:
- `base64-converter` - Interactive command-line interface
- `base64-converter-gui` - Launch web GUI
- `base64-converter-web` - Start web server

## 🐛 Troubleshooting

### **Installation Issues**

**"Package directory does not exist" error:**
```bash
# Run the quick setup first
python quick_setup.py

# Then try building again
python build_and_test.py
```

**"Missing required files" error:**
- Ensure all files are in the correct package structure
- Reinstall the package: `pip install --force-reinstall -e .`

### **Usage Issues**

**GUI won't start:**
```bash
# Check if the package is installed correctly
pip list | grep base64-image-converter

# Try running the module directly
python -m base64_image_converter.launch_gui
```

**Conversion failures:**
- Check the process log for detailed error messages
- Ensure input files are valid images or properly formatted base64 HTML
- Verify file permissions and disk space

**"Port already in use" error:**
- Close any existing instances of the application
- The system will automatically find an available port

### **Browser Issues**

**Browser won't open automatically:**
- Manually navigate to `http://localhost:8080`
- Check if your firewall is blocking the connection
- Try a different browser

## 📝 Version Information

- **Version**: 1.0.0
- **Release Date**: July 8, 2025
- **Author**: Data Team - Informatics Developer
- **Organization**: Healthcare Organization
- **License**: MIT License

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### **Development Setup**

```bash
# Clone the repository
git clone https://github.com/your-org/base64-image-converter.git
cd base64-image-converter

# Install in development mode
pip install -e .

# Run tests
python build_and_test.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋 Support

For questions, bug reports, or feature requests:

- **Internal Users**: Contact Data Team - Informatics Department
- **Issues**: Create an issue on the project repository
- **Documentation**: Check the built-in tutorial in the web interface

## 🎉 Acknowledgments

- Built for the Employee Recognition App project
- Developed by the Data Team - Informatics Department
- Designed for healthcare organization workflows

---

**Happy Converting!** 🚀

*Transform your images and base64 data with ease using our professional, feature-rich conversion tools.*
