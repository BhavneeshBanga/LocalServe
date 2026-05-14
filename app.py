from flask import Flask, send_from_directory, render_template_string
import os
import socket

app = Flask(__name__, static_folder='static')

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="UTF-8">
<title>File Drop</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">

<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg:       #0a0a0f;
    --surface:  #111118;
    --card:     #16161f;
    --border:   #2a2a3a;
    --accent:   #e8ff5a;
    --accent2:  #5afff0;
    --text:     #e8e8f0;
    --muted:    #5c5c72;
    --danger:   #ff5a5a;
  }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Syne', sans-serif;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 40px 16px 60px;
    position: relative;
    overflow-x: hidden;
  }

  /* Background grid */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(232,255,90,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(232,255,90,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  /* Glow orb */
  body::after {
    content: '';
    position: fixed;
    top: -200px;
    left: 50%;
    transform: translateX(-50%);
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(232,255,90,0.06) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
  }

  .wrapper {
    position: relative;
    z-index: 1;
    width: 100%;
    max-width: 560px;
  }

  /* Header */
  header {
    text-align: center;
    margin-bottom: 40px;
    animation: fadeDown 0.6s ease both;
  }

  .logo-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 100px;
    padding: 6px 16px;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    color: var(--muted);
    letter-spacing: 0.1em;
    margin-bottom: 20px;
  }

  .logo-dot {
    width: 6px;
    height: 6px;
    background: var(--accent);
    border-radius: 50%;
    animation: pulse 2s infinite;
  }

  h1 {
    font-size: clamp(2rem, 6vw, 3rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -0.03em;
  }

  h1 span {
    color: var(--accent);
  }

  .subtitle {
    margin-top: 10px;
    color: var(--muted);
    font-size: 14px;
    font-family: 'DM Mono', monospace;
  }

  /* Stats bar */
  .stats-bar {
    display: flex;
    gap: 12px;
    margin-bottom: 28px;
    animation: fadeUp 0.6s 0.1s ease both;
  }

  .stat {
    flex: 1;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px;
    text-align: center;
  }

  .stat-num {
    font-size: 22px;
    font-weight: 800;
    color: var(--accent);
  }

  .stat-label {
    font-size: 11px;
    color: var(--muted);
    font-family: 'DM Mono', monospace;
    margin-top: 2px;
    letter-spacing: 0.05em;
  }

  /* File list */
  .file-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .file-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 16px 18px;
    display: flex;
    align-items: center;
    gap: 14px;
    transition: border-color 0.2s, transform 0.2s, background 0.2s;
    animation: fadeUp 0.4s ease both;
    text-decoration: none;
    color: inherit;
    cursor: pointer;
  }

  .file-card:hover {
    border-color: var(--accent);
    background: #1a1a25;
    transform: translateY(-2px);
  }

  .file-card:active {
    transform: scale(0.98);
  }

  .file-icon {
    width: 42px;
    height: 42px;
    background: #1e1e2a;
    border: 1px solid var(--border);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
    transition: background 0.2s, border-color 0.2s;
  }

  .file-card:hover .file-icon {
    background: rgba(232,255,90,0.08);
    border-color: var(--accent);
  }

  .file-info {
    flex: 1;
    min-width: 0;
  }

  .file-name {
    font-size: 14px;
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    color: var(--text);
  }

  .file-meta {
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    color: var(--muted);
    margin-top: 3px;
  }

  .dl-btn {
    display: flex;
    align-items: center;
    gap: 6px;
    background: var(--accent);
    color: #0a0a0f;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 13px;
    border: none;
    border-radius: 8px;
    padding: 9px 14px;
    cursor: pointer;
    transition: transform 0.15s, opacity 0.15s;
    text-decoration: none;
    flex-shrink: 0;
  }

  .dl-btn:hover { opacity: 0.88; }
  .dl-btn:active { transform: scale(0.94); }

  .dl-btn svg {
    width: 14px;
    height: 14px;
    stroke: currentColor;
    fill: none;
    stroke-width: 2.5;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  /* Empty state */
  .empty {
    text-align: center;
    padding: 60px 20px;
    color: var(--muted);
    background: var(--surface);
    border: 1px dashed var(--border);
    border-radius: 16px;
  }

  .empty-icon {
    font-size: 40px;
    margin-bottom: 12px;
  }

  .empty p {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  /* Footer */
  footer {
    margin-top: 40px;
    text-align: center;
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    color: var(--muted);
    animation: fadeUp 0.6s 0.3s ease both;
  }

  footer span {
    color: var(--accent2);
  }

  /* Animations */
  @keyframes fadeDown {
    from { opacity: 0; transform: translateY(-20px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.3; }
  }

  /* Staggered cards */
  .file-card:nth-child(1)  { animation-delay: 0.15s; }
  .file-card:nth-child(2)  { animation-delay: 0.2s; }
  .file-card:nth-child(3)  { animation-delay: 0.25s; }
  .file-card:nth-child(4)  { animation-delay: 0.3s; }
  .file-card:nth-child(5)  { animation-delay: 0.35s; }
  .file-card:nth-child(6)  { animation-delay: 0.4s; }
  .file-card:nth-child(7)  { animation-delay: 0.45s; }
  .file-card:nth-child(8)  { animation-delay: 0.5s; }
  .file-card:nth-child(9)  { animation-delay: 0.55s; }
  .file-card:nth-child(10) { animation-delay: 0.6s; }
</style>
</head>

<body>
<div class="wrapper">

  <header>
    <div class="logo-badge">
      <span class="logo-dot"></span>
      LOCAL SERVER
    </div>
    <h1>File <span>Drop</span></h1>
    <p class="subtitle">// tap any file to download</p>
  </header>

  <div class="stats-bar">
    <div class="stat">
      <div class="stat-num">{{ files|length }}</div>
      <div class="stat-label">FILES</div>
    </div>
    <div class="stat">
      <div class="stat-num">{{ total_size }}</div>
      <div class="stat-label">TOTAL SIZE</div>
    </div>
  </div>

  {% if files %}
  <div class="file-list">
    {% for f in files %}
    <div class="file-card" onclick="window.location='/download/{{ f }}'">
      <div class="file-icon">{{ emoji_for(f) }}</div>
      <div class="file-info">
        <div class="file-name">{{ f }}</div>
        <div class="file-meta">{{ file_size(f) }}</div>
      </div>
      <a class="dl-btn" href="/download/{{ f }}" onclick="event.stopPropagation()">
        <svg viewBox="0 0 24 24"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
        Save
      </a>
    </div>
    {% endfor %}
  </div>

  {% else %}
  <div class="empty">
    <div class="empty-icon">📭</div>
    <p>No files in /static folder</p>
  </div>
  {% endif %}

  <footer>
    served locally &mdash; <span>http://{{ host }}:5163</span>
  </footer>

</div>
</body>
</html>
"""


def get_emoji(filename):
    ext = filename.rsplit('.', 1)[-1].lower() if '.' in filename else ''
    mapping = {
        'mp4': '🎬', 'mkv': '🎬', 'avi': '🎬', 'mov': '🎬', 'webm': '🎬',
        'mp3': '🎵', 'wav': '🎵', 'flac': '🎵', 'm4a': '🎵',
        'jpg': '🖼️', 'jpeg': '🖼️', 'png': '🖼️', 'gif': '🖼️', 'webp': '🖼️',
        'pdf': '📄', 'doc': '📝', 'docx': '📝', 'txt': '📝',
        'zip': '📦', 'rar': '📦', '7z': '📦', 'tar': '📦',
        'apk': '📱', 'exe': '⚙️', 'py': '🐍',
    }
    return mapping.get(ext, '📁')


def get_file_size(filename):
    try:
        path = os.path.join('static', filename)
        size = os.path.getsize(path)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"
    except:
        return "—"


def get_total_size(files):
    total = 0
    for f in files:
        try:
            total += os.path.getsize(os.path.join('static', f))
        except:
            pass
    for unit in ['B', 'KB', 'MB', 'GB']:
        if total < 1024:
            return f"{total:.1f} {unit}"
        total /= 1024
    return f"{total:.1f} TB"


@app.route('/')
def index():
    files = sorted(os.listdir('static')) if os.path.exists('static') else []
    host = socket.gethostbyname(socket.gethostname())
    return render_template_string(
        HTML,
        files=files,
        host=host,
        emoji_for=get_emoji,
        file_size=get_file_size,
        total_size=get_total_size(files),
    )


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('static', filename, as_attachment=True)


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return socket.gethostbyname(socket.gethostname())


def print_qr(url):
    """Generate and print QR code in terminal using qrcode library."""
    try:
        import qrcode
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Print QR in terminal using Unicode blocks
        print("\n" + "─" * 50)
        print(f"  📱  Scan to open on mobile")
        print(f"  🔗  {url}")
        print("─" * 50)
        qr.print_ascii(invert=True)
        print("─" * 50 + "\n")

    except ImportError:
        # Fallback: use api.qrserver.com URL if qrcode not installed
        print("\n" + "─" * 50)
        print(f"  📱  Mobile URL: {url}")
        print(f"  ⚠️   Install qrcode for terminal QR: pip install qrcode")
        print("─" * 50 + "\n")


if __name__ == "__main__":
    PORT = 5163
    local_ip = get_local_ip()
    url = f"http://{local_ip}:{PORT}"

    print_qr(url)

    app.run(host="0.0.0.0", port=PORT, debug=False)