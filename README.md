<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=180&section=header&text=LocalServe&fontSize=60&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=One-click%20File%20Downloads%20over%20LAN&descAlignY=60&descSize=18" width="100%"/>

# 📥 LocalServe

**Host any file on your laptop — download it instantly on any device over WiFi.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Made by Bhavneesh](https://img.shields.io/badge/Made%20by-BhavneeshBanga-764ba2?style=for-the-badge)](https://github.com/BhavneeshBanga)

</div>

---

## 🎯 What is LocalServe?

**LocalServe** is a dead-simple Flask server that turns your laptop into a **local file download hub**.

Drop files into the `/static` folder → run the server → anyone on the same WiFi can open the link and download directly from their phone or laptop. No cloud, no AirDrop, no sharing links.

Perfect for sharing videos, APKs, documents, or any large files across devices instantly.

---

## ✨ Features

- 🎬 Serves files from a **single `/static` folder** — just drop and go
- 📱 Beautiful **mobile-friendly UI** with download cards
- ⬇️ **One-tap download** on any browser
- 🔒 **100% local** — files stay on your network
- ⚡ Zero configuration — runs in seconds
- 🌐 Works on **any device** with a browser

---

## 🆚 LocalServe vs LocalDrop

| Feature | LocalServe | LocalDrop |
|---|---|---|
| Direction | Laptop → Phone | Phone → Laptop |
| Use case | Share files to others | Receive files from phone |
| UI | Download cards | Upload form |
| Setup | Drop files in `/static` | Upload via browser |

> Use both together for **two-way transfer**!

---

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)

---

## ⚙️ Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/BhavneeshBanga/LocalServe.git
cd LocalServe
```

### 2. Install dependencies

```bash
pip install flask
```

### 3. Add files to share

```bash
# Drop any file into the static folder
cp ~/Videos/myvideo.mp4 static/
cp ~/Documents/notes.pdf static/
```

### 4. Start the server

```bash
python app.py
```

### 5. Open on any device

Same WiFi pe koi bhi device kholo aur jaao:

```
http://<your-laptop-ip>:5163
```

> 💡 Find your laptop IP:
> - **Windows** → Run `ipconfig` → IPv4 Address
> - **Mac/Linux** → Run `ifconfig` or `ip a`

---

## 📁 Project Structure

```
LocalServe/
├── app.py          # Flask server
└── static/         # 📂 Drop your files here
    ├── video.mp4
    ├── document.pdf
    └── ...
```

---

## 🔄 How it works

```
💻 Laptop (Flask server running)
        |
        |  Reads files from /static folder
        |
        ▼
🌐 http://<laptop-ip>:5163
        |
        ├──── 📱 Phone opens link → sees file list → taps Download
        ├──── 💻 Friend's laptop → downloads in browser
        └──── 📺 Smart TV browser → streams video directly
```

---

## 🔮 Roadmap

- [ ] File size display on each card
- [ ] Video preview / thumbnail
- [ ] QR code on homepage for easy mobile access
- [ ] Folder support
- [ ] Password protection for sensitive files
- [ ] Drag & drop files into `/static` via UI

---

## 👨‍💻 Author

**Bhavneesh Banga** — B.Tech CSE 2nd Year | Full Stack & AI/ML

[![GitHub](https://img.shields.io/badge/GitHub-BhavneeshBanga-181717?style=flat&logo=github)](https://github.com/BhavneeshBanga)
[![LeetCode](https://img.shields.io/badge/LeetCode-BhavneeshBanga-FFA116?style=flat&logo=leetcode&logoColor=black)](https://leetcode.com/BhavneeshBanga)

---

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" width="100%"/>