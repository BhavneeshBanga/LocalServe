from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__, static_folder='static')

# Home page – shows list of files inside /static folder
@app.route('/')
def index():
    files = os.listdir('static')
    
    html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Download Files</title>

<style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #667eea, #764ba2);
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }

    .container {
        width: 95%;
        max-width: 500px;
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }

    h2 {
        text-align: center;
        margin-bottom: 20px;
        color: #333;
    }

    ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    li {
        margin-bottom: 15px;
    }

    .file-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px;
        border-radius: 12px;
        background: #f4f6ff;
        transition: 0.3s ease;
    }

    .file-card:hover {
        background: #e2e6ff;
    }

    .file-name {
        font-size: 14px;
        word-break: break-all;
        color: #444;
    }

    .download-btn {
        padding: 10px 15px;
        border: none;
        border-radius: 8px;
        background: #667eea;
        color: white;
        font-size: 14px;
        text-decoration: none;
        font-weight: bold;
        transition: 0.3s;
    }

    .download-btn:active {
        transform: scale(0.95);
        background: #5a67d8;
    }

    .empty {
        text-align: center;
        color: gray;
        padding: 20px;
    }
</style>
</head>

<body>
    <div class="container">
        <h2>📥 Download Videos</h2>

        {% if files %}
        <ul>
            {% for f in files %}
            <li>
                <div class="file-card">
                    <div class="file-name">🎬 {{ f }}</div>
                    <a class="download-btn" href="/download/{{ f }}">
                        ⬇ Download
                    </a>
                </div>
            </li>
            {% endfor %}
        </ul>
        {% else %}
            <div class="empty">No files available</div>
        {% endif %}
    </div>
</body>
</html>
"""

    return render_template_string(html, files=files)

# Route for downloading files
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('static', filename, as_attachment=True)

if __name__ == "__main__":
    # 0.0.0.0 → makes it accessible on phone over same WiFi
    app.run(host="0.0.0.0", port=5163, debug=False)
