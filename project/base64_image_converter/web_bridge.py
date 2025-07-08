#!/usr/bin/env python3
"""
=====================================================================================
                    WEB INTERFACE BRIDGE FOR BASE64 CONVERTER
=====================================================================================

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
=====================================================================================

This script provides a web server bridge to integrate the HTML GUI with the 
base64 image converter Python script. It creates a local web server that can
handle file uploads and conversion requests from the HTML interface.

Usage:
    python web_bridge.py

Then open your browser to: http://localhost:8080
"""

import os
import json
import shutil
import tempfile
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import webbrowser
import threading
import time

# Try to use modern importlib.resources, fallback to pkg_resources
try:
    from importlib import resources
    MODERN_IMPORT = True
except ImportError:
    try:
        import pkg_resources
        MODERN_IMPORT = False
    except ImportError:
        print("⚠️  Warning: Neither importlib.resources nor pkg_resources available")
        MODERN_IMPORT = None

# Import your existing converter functions
try:
    from .convertIMAGE_script import process_file, file_size_str
except ImportError:
    try:
        from convertIMAGE_script import process_file, file_size_str
    except ImportError:
        print("⚠️  Warning: Could not import convertIMAGE_script. Make sure it's in the same directory.")
        # Fallback function for demonstration
        def process_file(file_path, output_dir):
            print(f"Demo: Would process {file_path} to {output_dir}")
            return True
        
        def file_size_str(file_path):
            return "Unknown size"

def get_package_file_path(filename):
    """Get the path to a file within the package"""
    try:
        if MODERN_IMPORT:
            # Use modern importlib.resources
            try:
                import base64_image_converter
                with resources.files(base64_image_converter).joinpath(filename) as f:
                    return str(f)
            except:
                # Fallback for older Python versions with importlib.resources
                with resources.path('base64_image_converter', filename) as f:
                    return str(f)
        elif MODERN_IMPORT is False:
            # Use pkg_resources
            return pkg_resources.resource_filename('base64_image_converter', filename)
        else:
            # No resource system available, fallback to current directory
            script_dir = os.path.dirname(os.path.abspath(__file__))
            return os.path.join(script_dir, filename)
    except:
        # Final fallback to current directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, filename)

class ConversionHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests - serve the HTML interface"""
        path = urlparse(self.path).path
        
        if path == '/' or path == '/index.html':
            self.serve_html_file()
        elif path == '/status':
            self.serve_status()
        elif path.startswith('/download/'):
            self.handle_download()
        else:
            self.send_error(404)
    
    def do_POST(self):
        """Handle POST requests - file uploads and conversion"""
        path = urlparse(self.path).path
        
        if path == '/convert':
            self.handle_conversion()
        else:
            self.send_error(404)
    
    def serve_html_file(self):
        """Serve the main HTML interface"""
        try:
            # Get the HTML file from package resources
            html_file = get_package_file_path('Base64_Converter_GUI.html')
            
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Inject JavaScript for Python integration
            integration_js = """
            <script>
            // Override the callPythonScript function to use the web bridge
            function callPythonScript(files, outputDir, mode) {
                return fetch('/convert', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        files: files,
                        outputDir: outputDir,
                        mode: mode
                    })
                })
                .then(response => response.json())
                .then(data => {
                    return data;
                })
                .catch(error => {
                    console.error('Error:', error);
                    throw error;
                });
            }

            // Enhanced file processing that uses the Python backend
            async function processFiles() {
                const totalFiles = selectedFiles.length;
                let processedFiles = 0;
                conversionResults = [];

                for (let i = 0; i < selectedFiles.length; i++) {
                    const file = selectedFiles[i];
                    const conversionDirection = determineConversionDirection(file.name);
                    
                    logMessage('info', `[${i + 1}/${totalFiles}] ${conversionDirection}: ${file.name}`);
                    
                    try {
                        // Convert file to base64 for transmission
                        const fileData = await fileToBase64(file);
                        
                        const response = await fetch('/convert', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({
                                fileName: file.name,
                                fileData: fileData,
                                fileSize: file.size,
                                conversionMode: document.getElementById('conversionMode').value
                            })
                        });
                        
                        const result = await response.json();
                        
                        if (result.success) {
                            conversionResults.push({
                                success: true,
                                inputFile: file.name,
                                outputFile: result.outputFile,
                                conversionType: conversionDirection,
                                fileSize: formatFileSize(file.size),
                                downloadUrl: result.downloadUrl
                            });
                            logMessage('success', `✅ Successfully converted: ${file.name} → ${result.outputFile}`);
                        } else {
                            conversionResults.push({
                                success: false,
                                inputFile: file.name,
                                error: result.error,
                                conversionType: conversionDirection
                            });
                            logMessage('error', `❌ Failed to convert: ${file.name} - ${result.error}`);
                        }
                    } catch (error) {
                        conversionResults.push({
                            success: false,
                            inputFile: file.name,
                            error: error.message,
                            conversionType: conversionDirection
                        });
                        logMessage('error', `❌ Error processing: ${file.name} - ${error.message}`);
                    }
                    
                    processedFiles++;
                    updateProgress((processedFiles / totalFiles) * 100);
                }
                
                finishConversion();
            }

            // Helper function to convert file to base64
            function fileToBase64(file) {
                return new Promise((resolve, reject) => {
                    const reader = new FileReader();
                    reader.readAsDataURL(file);
                    reader.onload = () => resolve(reader.result);
                    reader.onerror = error => reject(error);
                });
            }

            // Update the displayResults function to handle download links
            function displayResults() {
                const resultsSection = document.getElementById('resultsSection');
                const resultsGrid = document.getElementById('resultsGrid');
                
                resultsGrid.innerHTML = '';
                
                conversionResults.forEach(result => {
                    const resultCard = document.createElement('div');
                    resultCard.className = `result-card ${result.success ? '' : 'error'}`;
                    
                    if (result.success) {
                        resultCard.innerHTML = `
                            <h4 style="color: var(--success-color); margin-bottom: 10px;">✅ ${result.inputFile}</h4>
                            <p><strong>Conversion:</strong> ${result.conversionType}</p>
                            <p><strong>Output:</strong> ${result.outputFile}</p>
                            <p><strong>Size:</strong> ${result.fileSize}</p>
                            <button class="btn" style="margin-top: 10px; padding: 5px 10px; font-size: 0.8rem;" 
                                    onclick="window.open('${result.downloadUrl}', '_blank')">
                                💾 Download
                            </button>
                        `;
                    } else {
                        resultCard.innerHTML = `
                            <h4 style="color: var(--error-color); margin-bottom: 10px;">❌ ${result.inputFile}</h4>
                            <p><strong>Conversion:</strong> ${result.conversionType}</p>
                            <p><strong>Error:</strong> ${result.error}</p>
                            <button class="btn" style="margin-top: 10px; padding: 5px 10px; font-size: 0.8rem;">
                                🔄 Retry
                            </button>
                        `;
                    }
                    
                    resultsGrid.appendChild(resultCard);
                });
                
                resultsSection.style.display = 'block';
            }
            </script>
            """
            
            # Insert the JavaScript before the closing body tag
            html_content = html_content.replace('</body>', integration_js + '</body>')
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('Content-length', len(html_content.encode('utf-8')))
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))
            
        except FileNotFoundError:
            self.send_error(404, "HTML interface file not found")
        except Exception as e:
            self.send_error(500, f"Error serving HTML: {str(e)}")
    
    def handle_conversion(self):
        """Handle file conversion requests"""
        try:
            # Read the request data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode('utf-8'))
            
            # Extract file information
            file_name = request_data['fileName']
            file_data = request_data['fileData']
            conversion_mode = request_data.get('conversionMode', 'auto')
            
            # Create temporary directories
            temp_input_dir = tempfile.mkdtemp(prefix='converter_input_')
            temp_output_dir = tempfile.mkdtemp(prefix='converter_output_')
            
            try:
                # Decode the base64 file data and save to temp input directory
                if file_data.startswith('data:'):
                    # Remove data URL prefix
                    header, data = file_data.split(',', 1)
                    file_content = data
                else:
                    file_content = file_data
                
                import base64
                binary_data = base64.b64decode(file_content)
                
                temp_input_file = os.path.join(temp_input_dir, file_name)
                with open(temp_input_file, 'wb') as f:
                    f.write(binary_data)
                
                # Process the file using your existing function
                success = process_file(temp_input_file, temp_output_dir)
                
                if success:
                    # Find the output file
                    output_files = os.listdir(temp_output_dir)
                    if output_files:
                        output_file = output_files[0]
                        output_path = os.path.join(temp_output_dir, output_file)
                        
                        # Create a download endpoint for the file
                        download_id = str(int(time.time() * 1000))  # Simple unique ID
                        
                        # Store the file for download (in a real app, use a proper storage system)
                        if not hasattr(self.server, 'download_files'):
                            self.server.download_files = {}
                        
                        with open(output_path, 'rb') as f:
                            self.server.download_files[download_id] = {
                                'data': f.read(),
                                'filename': output_file,
                                'created': time.time()
                            }
                        
                        response = {
                            'success': True,
                            'outputFile': output_file,
                            'downloadUrl': f'/download/{download_id}',
                            'message': 'Conversion completed successfully'
                        }
                    else:
                        response = {
                            'success': False,
                            'error': 'No output file generated'
                        }
                else:
                    response = {
                        'success': False,
                        'error': 'Conversion failed'
                    }
                
            finally:
                # Clean up temporary directories
                shutil.rmtree(temp_input_dir, ignore_errors=True)
                shutil.rmtree(temp_output_dir, ignore_errors=True)
            
            # Send response
            response_json = json.dumps(response)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Content-length', len(response_json.encode('utf-8')))
            self.end_headers()
            self.wfile.write(response_json.encode('utf-8'))
            
        except Exception as e:
            error_response = json.dumps({
                'success': False,
                'error': str(e)
            })
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Content-length', len(error_response.encode('utf-8')))
            self.end_headers()
            self.wfile.write(error_response.encode('utf-8'))
    
    def handle_download(self):
        """Handle file download requests"""
        try:
            # Extract download ID from path
            path = urlparse(self.path).path
            download_id = path.split('/')[-1]
            
            # Check if we have the download file
            if not hasattr(self.server, 'download_files') or download_id not in self.server.download_files:
                self.send_error(404, "Download file not found or expired")
                return
            
            file_info = self.server.download_files[download_id]
            file_data = file_info['data']
            filename = file_info['filename']
            
            # Determine content type based on file extension
            content_type = 'application/octet-stream'
            if filename.lower().endswith(('.txt', '.b64')):
                content_type = 'text/plain'
            elif filename.lower().endswith(('.jpg', '.jpeg')):
                content_type = 'image/jpeg'
            elif filename.lower().endswith('.png'):
                content_type = 'image/png'
            elif filename.lower().endswith('.gif'):
                content_type = 'image/gif'
            
            # Send the file
            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
            self.send_header('Content-Length', len(file_data))
            self.end_headers()
            self.wfile.write(file_data)
            
            print(f"✅ File downloaded: {filename} ({len(file_data)} bytes)")
            
        except Exception as e:
            print(f"❌ Download error: {e}")
            self.send_error(500, f"Download error: {str(e)}")
    
    def serve_status(self):
        """Serve application status"""
        status = {
            'status': 'ready',
            'message': 'Base64 Converter Web Interface is running'
        }
        response_json = json.dumps(status)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-length', len(response_json.encode('utf-8')))
        self.end_headers()
        self.wfile.write(response_json.encode('utf-8'))

def cleanup_old_downloads(server, max_age=3600):
    """Clean up old download files (older than max_age seconds)"""
    if hasattr(server, 'download_files'):
        current_time = time.time()
        to_remove = []
        for download_id, file_info in server.download_files.items():
            if current_time - file_info['created'] > max_age:
                to_remove.append(download_id)
        
        for download_id in to_remove:
            del server.download_files[download_id]

def start_cleanup_thread(server):
    """Start a background thread to clean up old files"""
    def cleanup_worker():
        while True:
            time.sleep(300)  # Clean up every 5 minutes
            cleanup_old_downloads(server)
    
    cleanup_thread = threading.Thread(target=cleanup_worker, daemon=True)
    cleanup_thread.start()

def main():
    """Start the web server"""
    port = 8080
    server_address = ('localhost', port)
    
    print("=" * 80)
    print("          BASE64 IMAGE CONVERTER - WEB INTERFACE")
    print("=" * 80)
    print(f"🚀 Starting web server on http://localhost:{port}")
    print("📂 Make sure Base64_Converter_GUI.html is in the same directory")
    print("🔧 Python script integration: ACTIVE")
    print()
    
    try:
        httpd = HTTPServer(server_address, ConversionHandler)
        httpd.download_files = {}  # Storage for download files
        
        # Start cleanup thread
        start_cleanup_thread(httpd)
        
        print(f"✅ Server started successfully!")
        print(f"🌐 Open your browser to: http://localhost:{port}")
        print("⏹️  Press Ctrl+C to stop the server")
        print()
        
        # Automatically open the browser
        threading.Timer(1.0, lambda: webbrowser.open(f'http://localhost:{port}')).start()
        
        # Start serving
        httpd.serve_forever()
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    main()
