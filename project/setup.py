#!/usr/bin/env python3
"""
Setup script for the Bidirectional Base64 Image Converter

This script handles the installation and packaging of the Base64 Image Converter
utility, including both the command-line interface and web-based GUI.
"""

from setuptools import setup, find_packages
import os

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
root_directory = os.path.dirname(this_directory)  # Go up to project root
with open(os.path.join(root_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements from requirements.txt if it exists
def read_requirements():
    requirements_path = os.path.join(this_directory, 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="base64-image-converter",
    version="1.0.0",
    author="KCoderVA",
    author_email="developer@kcoder.dev",
    description="Bidirectional converter for images and base64-encoded HTML format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KCoderVA/Base64_ImageConverter",
    project_urls={
        "Bug Tracker": "https://github.com/KCoderVA/Base64_ImageConverter/issues",
        "Documentation": "https://github.com/KCoderVA/Base64_ImageConverter/wiki",
        "Source Code": "https://github.com/KCoderVA/Base64_ImageConverter",
        "Download": "https://github.com/KCoderVA/Base64_ImageConverter/releases",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Environment :: Web Environment",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "gui": [
            "tkinter",  # Usually included with Python
        ],
    },
    entry_points={
        "console_scripts": [
            "base64-converter=base64_image_converter.convertIMAGE_script:main",
            "base64-converter-gui=base64_image_converter.launch_gui:main",
            "base64-converter-web=base64_image_converter.web_bridge:main",
        ],
    },
    include_package_data=True,
    package_data={
        "base64_image_converter": [
            "*.html",
            "*.css",
            "*.js",
        ],
        "": [
            "*.md",
            "*.txt",
            "Inputs/*",
            "Outputs/*",
        ],
    },
    zip_safe=False,
    keywords=[
        "base64",
        "image",
        "converter",
        "html",
        "encoding",
        "decoding",
        "web",
        "gui",
        "bidirectional",
        "healthcare",
        "informatics",
    ],
)
