# Installation Guide

## Quick Installation

### Method 1: Install from Wheel (Recommended)
1. Download the latest `.whl` file from the releases
2. Install using pip:
   ```bash
   pip install base64_image_converter-1.0.0-py3-none-any.whl
   ```

### Method 2: Install from Source
1. Download and extract the source code
2. Navigate to the project directory
3. Install using pip:
   ```bash
   pip install .
   ```

### Method 3: Development Installation
For developers who want to modify the code:
```bash
pip install -e .
```

## Verify Installation

After installation, verify that the commands are available:

```bash
# Test CLI interface
base64-converter --help

# Test GUI launcher
base64-converter-gui

# Test web interface
base64-converter-web
```

## System Requirements

- Python 3.6 or higher
- Windows, macOS, or Linux
- No external dependencies (uses Python standard library only)

## Post-Installation

### Command Line Usage
```bash
# Convert image to base64 HTML
base64-converter input.jpg output.html

# Extract image from base64 HTML
base64-converter input.html extracted.jpg
```

### GUI Usage
```bash
# Launch web-based GUI
base64-converter-gui
```

This will:
1. Start a local web server
2. Open your default browser
3. Display the conversion interface

### Web Server Usage
```bash
# Start just the web server (for integration)
base64-converter-web --port 8080
```

## Troubleshooting

### Command Not Found
If you get "command not found" errors:

1. **Check Python installation**: Ensure Python is installed and in your PATH
2. **Check pip installation**: Verify the package was installed: `pip list | grep base64`
3. **Check PATH**: The scripts should be in your Python scripts directory
4. **Virtual Environment**: If using a virtual environment, ensure it's activated

### Permission Errors
If you get permission errors during installation:

1. **Use --user flag**: `pip install --user base64_image_converter-1.0.0-py3-none-any.whl`
2. **Use virtual environment**: Create and activate a virtual environment first

### Import Errors
If you get import errors:
1. **Check Python version**: Ensure you're using Python 3.6+
2. **Reinstall**: Try uninstalling and reinstalling the package

## Uninstallation

To remove the package:
```bash
pip uninstall base64-image-converter
```

## Getting Help

- Check the README.md for detailed usage instructions
- Review the CONTRIBUTING.md for development guidelines
- Open an issue on the project repository for bugs or feature requests
