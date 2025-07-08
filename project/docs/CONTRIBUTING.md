# Contributing to Base64 Image Converter

Thank you for your interest in contributing to the Bidirectional Base64 Image Converter! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Issue Reporting](#issue-reporting)
- [Contact](#contact)

## 🤝 Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming and inclusive environment. By participating, you are expected to uphold professional standards and treat all contributors with respect.

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Git for version control
- A text editor or IDE of your choice
- Basic knowledge of Python programming

### Initial Setup

1. **Fork the repository** on your preferred platform
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/base64-image-converter.git
   cd base64-image-converter
   ```
3. **Create a development branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🛠️ Development Setup

### Local Environment

1. **Ensure Python 3.6+ is installed**:
   ```bash
   python --version
   ```

2. **Install development dependencies** (optional):
   ```bash
   pip install pytest pytest-cov black flake8 mypy
   ```

3. **Test the installation**:
   ```bash
   python convertIMAGE_script.py --help
   python launch_gui.py
   ```

### Project Structure

```
base64-image-converter/
├── convertIMAGE_script.py      # Main conversion engine
├── Base64_Converter_GUI.html   # Web interface
├── web_bridge.py               # Web server bridge
├── launch_gui.py               # GUI launcher
├── setup.py                    # Package setup
├── requirements.txt            # Dependencies
├── README.md                   # Project documentation
├── LICENSE                     # License information
├── CHANGELOG.md               # Version history
├── CONTRIBUTING.md            # This file
├── Inputs/                    # Default input directory
└── Outputs/                   # Default output directory
```

## 📝 Contributing Guidelines

### Types of Contributions

We welcome several types of contributions:

- **🐛 Bug Reports**: Report issues and problems
- **✨ Feature Requests**: Suggest new functionality
- **📖 Documentation**: Improve or add documentation
- **🔧 Code Improvements**: Enhance existing functionality
- **🧪 Testing**: Add or improve test coverage
- **🎨 UI/UX**: Improve the user interface and experience

### Before Contributing

1. **Search existing issues** to avoid duplicates
2. **Read the documentation** to understand current functionality
3. **Test the current version** to reproduce any issues
4. **Discuss major changes** before implementing them

## 🔄 Pull Request Process

### Preparation

1. **Ensure your fork is up to date**:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a focused branch**:
   ```bash
   git checkout -b fix/issue-description
   # or
   git checkout -b feature/feature-description
   ```

### Development

1. **Make your changes** following the coding standards
2. **Test your changes** thoroughly
3. **Update documentation** if necessary
4. **Add appropriate comments** and docstrings

### Submission

1. **Commit your changes** with clear messages:
   ```bash
   git add .
   git commit -m "Add: Brief description of changes"
   ```

2. **Push to your fork**:
   ```bash
   git push origin your-branch-name
   ```

3. **Create a pull request** with:
   - Clear title and description
   - Reference to related issues
   - Screenshots for UI changes
   - Testing instructions

### Review Process

- Maintainers will review your pull request
- Address any requested changes
- Once approved, your contribution will be merged

## 📏 Coding Standards

### Python Code Style

- **Follow PEP 8** guidelines for Python code
- **Use meaningful variable names** and function names
- **Add docstrings** to all functions and classes
- **Include type hints** where appropriate
- **Limit line length** to 88 characters (Black formatter standard)

### Code Formatting

Use Black for automatic code formatting:
```bash
black convertIMAGE_script.py web_bridge.py launch_gui.py
```

### Linting

Use flake8 for code linting:
```bash
flake8 *.py --max-line-length=88 --extend-ignore=E203,W503
```

### Example Code Structure

```python
def process_image(image_path: str, output_dir: str) -> bool:
    """
    Convert a single image file to base64-encoded HTML format.
    
    Args:
        image_path (str): Full path to the source image file
        output_dir (str): Directory where the output file will be saved
    
    Returns:
        bool: True if conversion successful, False otherwise
    
    Raises:
        FileNotFoundError: If the input image file doesn't exist
        PermissionError: If unable to write to output directory
    """
    # Implementation here
    pass
```

## 🧪 Testing

### Manual Testing

1. **Test basic functionality**:
   - Image to base64 conversion
   - Base64 to image conversion
   - Batch processing
   - GUI interface

2. **Test edge cases**:
   - Large files
   - Invalid file formats
   - Corrupted files
   - Empty directories

3. **Cross-platform testing**:
   - Windows
   - macOS
   - Linux

### Automated Testing (Future)

We plan to add automated testing. Contributors are welcome to help set up:
- Unit tests with pytest
- Integration tests
- UI tests for the web interface

## 📚 Documentation

### Code Documentation

- **Add docstrings** to all public functions
- **Include parameter descriptions** and return values
- **Document exceptions** that may be raised
- **Provide usage examples** for complex functions

### User Documentation

- **Update README.md** for new features
- **Add examples** to demonstrate usage
- **Update help text** and command-line options
- **Include screenshots** for GUI changes

## 🐛 Issue Reporting

### Bug Reports

When reporting bugs, please include:

- **Python version** and operating system
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Error messages** or screenshots
- **Sample files** that cause the issue (if applicable)

### Feature Requests

For feature requests, provide:

- **Clear description** of the requested feature
- **Use case** and rationale
- **Proposed implementation** approach (if you have ideas)
- **Potential impact** on existing functionality

## 🎯 Development Focus Areas

We're particularly interested in contributions in these areas:

1. **Performance Optimization**: Faster processing for large files
2. **Additional File Formats**: Support for TIFF, WebP, SVG
3. **Error Handling**: More robust error detection and recovery
4. **User Interface**: Improvements to the web-based GUI
5. **Testing Framework**: Automated testing setup
6. **Documentation**: Examples, tutorials, and API documentation
7. **Accessibility**: Making the interface more accessible
8. **Internationalization**: Multi-language support

## 📞 Contact

### Getting Help

- **File an issue** for bugs or feature requests
- **Start a discussion** for questions about contributing
- **Email the team**: Data Team - Informatics Department

### Maintainers

- **Primary Maintainer**: Data Team - Informatics Developer
- **Organization**: Healthcare Organization
- **Department**: Data Team - Informatics

## 🙏 Recognition

Contributors will be recognized in:
- The project README.md file
- Release notes and changelog
- Project documentation

Thank you for contributing to the Base64 Image Converter! Your efforts help make this tool better for everyone in the healthcare informatics community and beyond.

---

**Happy Coding!** 🚀
