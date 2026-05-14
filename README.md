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
- 📊 Shows **file sizes** and **total storage** used
- 📷 **QR code** in terminal — scan and open instantly on mobile

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
pip install flask qrcode
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

A **QR code** will appear in your terminal — scan it with your phone camera and it opens instantly in the browser. Or navigate manually on any same-WiFi device:

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

## 🧠 Deep Dive — How Your 0s and 1s Actually Travel

> **"Every file you see on screen is secretly a river of 0s and 1s flowing through invisible electromagnetic waves. Here's the full journey."**

This section explains — from first principles — exactly what happens when you tap **Download** on your phone and a video file lands on it from your laptop. We go from the bits stored on disk all the way to the bits arriving at your phone. No step is skipped.

---

### 📦 Stage 1 — The File on Disk (How Storage Works)

Every file on your laptop — your `.mp4`, `.pdf`, `.apk` — is ultimately stored as **billions of tiny magnetic or electrical states** on your hard drive or SSD.

#### On an HDD (Hard Disk Drive):
- The disk is a spinning metal platter coated with magnetic material.
- A `1` is stored by magnetizing a tiny region in one direction (e.g., North).
- A `0` is stored by magnetizing it the other way (South).
- The read/write head flies nanometers above the spinning platter at 7200 RPM and reads these magnetic polarities at millions of bits per second.

#### On an SSD (Solid State Drive):
- No moving parts. Instead, billions of **floating-gate transistors** store charge.
- A transistor with charge trapped inside = `1`. No charge = `0`.
- SSDs can store 2 bits (MLC), 3 bits (TLC), or even 4 bits (QLC) per cell by using multiple voltage levels — for example, 0V = `00`, 1V = `01`, 2V = `10`, 3V = `11`.

#### What a file actually looks like in binary:
A PDF starts with this magic header (called a **file signature**) which tells the OS what kind of file it is:

```
Binary on disk:   00100101 01010000 01000100 01000110
As hex:           25       50       44       46
As ASCII:         %        P        D        F
```

The OS filesystem (NTFS on Windows, ext4 on Linux, APFS on Mac) keeps a **table of contents** called an inode or MFT entry that says: "this file called `notes.pdf` starts at disk block 4821 and spans 320 blocks." When Python's Flask calls `open("notes.pdf")`, the OS reads that map and fetches the right magnetic/electrical bits from disk.

---

### 🧱 Stage 2 — The File Enters RAM

The OS doesn't send file bytes directly from disk to network. They first move into **RAM (Random Access Memory)**.

RAM is made of **capacitors and transistors** arranged in a grid:
- A charged capacitor = `1`
- A discharged capacitor = `0`

RAM is volatile (loses data when power is cut) but is ~1000× faster than SSDs. The bytes of your file sit here temporarily, waiting to be processed by Flask and sent over the network.

In our Flask app, this happens implicitly:

```python
# Flask internally does something like this:
with open('static/video.mp4', 'rb') as f:
    data = f.read()   # File bytes now live in RAM
    # send() pushes them out to the network socket
```

---

### 🌐 Stage 3 — The Networking Stack (Where the Magic Begins)

When your phone's browser makes a request and Flask responds with file bytes, those bytes do NOT jump directly through the air. They descend through a **stack of layers**, each adding its own wrapper of information — like putting a letter inside an envelope inside a box inside a shipping container.

This is called the **TCP/IP Network Stack** (also called the OSI model).

```
Your File Bytes (Application Data)
         │
         ▼
┌─────────────────────────────────┐
│  Layer 7 — APPLICATION (HTTP)   │  Flask adds HTTP headers
├─────────────────────────────────┤
│  Layer 4 — TRANSPORT (TCP)      │  Splits into segments, adds port numbers
├─────────────────────────────────┤
│  Layer 3 — NETWORK (IP)         │  Adds source/destination IP addresses
├─────────────────────────────────┤
│  Layer 2 — DATA LINK (Ethernet) │  Adds MAC addresses, creates frames
├─────────────────────────────────┤
│  Layer 1 — PHYSICAL (WiFi/Wire) │  Converts frames → electromagnetic waves
└─────────────────────────────────┘
```

Let's walk through each layer.

---

#### 🔵 Layer 7 — Application Layer (HTTP)

Flask speaks **HTTP (HyperText Transfer Protocol)**.

When your phone's browser hits `/download/video.mp4`, Flask constructs an HTTP response that looks like this in raw text (which is also just binary on the wire):

```
HTTP/1.1 200 OK\r\n
Content-Type: video/mp4\r\n
Content-Length: 104857600\r\n
Content-Disposition: attachment; filename="video.mp4"\r\n
\r\n
[raw binary bytes of the video file start here]
```

The **header** (the text part above) tells your phone: "What's coming is 100 MB of mp4 video data." Then the actual file bytes follow immediately after the blank line — as raw binary, exactly as they were on disk.

---

#### 🟡 Layer 4 — Transport Layer (TCP)

The HTTP response (headers + file bytes) can be 100 MB or more. You cannot send that as a single chunk — the network infrastructure can't handle it. So **TCP (Transmission Control Protocol)** breaks it into small pieces called **segments**.

Each TCP segment is typically **1460 bytes** of actual data (called MSS — Maximum Segment Size).

A 100 MB file = 100 × 1024 × 1024 = **104,857,600 bytes** → divided into roughly **71,820 TCP segments**.

Each segment gets a **TCP header** added to the front:

```
┌──────────────────────────────────────────────────────┐
│ Source Port: 5163 │ Destination Port: 54231          │
│ Sequence Number: 0000014600  (which byte this starts)│
│ Acknowledgment Number: ...                           │
│ Flags: [ACK] [PSH]                                   │
│ Window Size: 65535                                   │
├──────────────────────────────────────────────────────┤
│ DATA: 1460 bytes of your video file                  │
└──────────────────────────────────────────────────────┘
```

**Why sequence numbers matter:** If segment #5 arrives before segment #3 (because WiFi is chaotic), TCP uses sequence numbers to **reassemble them in the correct order** on the phone side. TCP also makes your phone send back an **ACK (acknowledgment)** for every segment received. If an ACK doesn't arrive, your laptop **resends** that segment — TCP guarantees every byte arrives correctly.

Port numbers are like apartment numbers in a building — the IP address gets you to the right building (device), and the port number gets you to the right room (application). Flask listens on port `5163`, your phone's browser connects from a random high port like `54231`.

---

#### 🟠 Layer 3 — Network Layer (IP)

Now each TCP segment gets wrapped in an **IP packet** by adding another header:

```
┌──────────────────────────────────────────────────────┐
│ Source IP:      192.168.1.10   (your laptop)         │
│ Destination IP: 192.168.1.25   (your phone)          │
│ TTL: 64   Protocol: TCP   Header Checksum: 0xA3F2    │
├──────────────────────────────────────────────────────┤
│ [TCP Header + 1460 bytes of video data]              │
└──────────────────────────────────────────────────────┘
```

**IP addresses** are like postal addresses. Both your laptop and phone have been assigned IP addresses by your WiFi router (via DHCP — Dynamic Host Configuration Protocol) when they joined the network. The router uses these addresses to decide where to forward each packet.

**TTL (Time To Live)** is a counter that decrements at each "hop." If a packet gets lost in a routing loop, TTL hits 0 and the packet is discarded — preventing infinite loops.

---

#### 🟢 Layer 2 — Data Link Layer (Ethernet/WiFi Frame)

Now the IP packet gets wrapped in an **Ethernet frame** (even over WiFi, the same concept applies):

```
┌────────────────────────────────────────────────────────────┐
│ Destination MAC: A4:C3:F0:12:44:B1   (your phone's WiFi)  │
│ Source MAC:      B8:27:EB:55:91:C0   (your laptop's WiFi)  │
│ EtherType: 0x0800  (IPv4)                                  │
├────────────────────────────────────────────────────────────┤
│ [IP Header + TCP Header + 1460 bytes of video data]        │
├────────────────────────────────────────────────────────────┤
│ FCS: 0xD3A92F11  (Frame Check Sequence — error detection)  │
└────────────────────────────────────────────────────────────┘
```

**MAC addresses** are hardware addresses burned into every WiFi/Ethernet chip during manufacturing — they're globally unique. While IP addresses are like postal addresses (can change), MAC addresses are like your Aadhaar number (permanent identity of the device).

**FCS (Frame Check Sequence)** is a CRC checksum — a mathematical fingerprint of all the bits in the frame. If even one bit flips during transmission, the FCS won't match and the frame is discarded and retransmitted.

---

#### 🔴 Layer 1 — Physical Layer (The 0s and 1s Go Airborne)

This is where your data **leaves the world of silicon** and becomes **electromagnetic energy**.

Your laptop's WiFi chip takes the Ethernet frame — now a very long sequence of `0`s and `1`s — and needs to transmit it wirelessly.

**How does a `1` or `0` travel through the air?**

WiFi uses **radio waves** (electromagnetic waves in the 2.4 GHz or 5 GHz frequency bands). The chip uses a technique called **modulation** to encode bits into these waves.

Modern WiFi (WiFi 5 / 802.11ac) uses **QAM (Quadrature Amplitude Modulation)**:

```
Modulation   Bits per Symbol   Speeds
─────────────────────────────────────────
BPSK         1 bit             Slowest, most reliable
QPSK         2 bits            ↑
16-QAM       4 bits            ↑
64-QAM       6 bits            ↑
256-QAM      8 bits            ↑
1024-QAM     10 bits           Fastest (WiFi 6)
```

With **256-QAM**, each "symbol" (one tiny fluctuation in the radio wave) carries **8 bits** of data. The WiFi chip changes the wave's **amplitude** (height) and **phase** (timing) 78 million times per second to encode all your bits.

**Visualizing a single bit traveling through air:**

```
Laptop WiFi Chip                           Phone WiFi Chip
      │                                           │
      │  Bit = 1 → shift radio wave phase by 90°  │
      │  ~~~/~~~\~~~~ → ~~~~\~~~~/~~~~            │
      │                                           │
      │  Radio wave travels at speed of light     │
      │  ────────────────────────────────────>    │
      │  (3 × 10⁸ m/s, reaches phone in ~3 ns)   │
      │                                           │
      │                         Phase shift = 90°?│
      │                              → Decode: 1  │
```

Your phone's WiFi chip is doing this for millions of symbols per second — receiving the radio waves, measuring their amplitude and phase, and converting them back to `0`s and `1`s.

**What about interference?** WiFi uses a technique called **OFDM (Orthogonal Frequency Division Multiplexing)** — instead of one radio channel, the data is split across **52 sub-channels** simultaneously. If one sub-channel gets interference (from a microwave oven, a neighbor's router), only a tiny fraction of the data is affected and TCP retransmits those few lost packets.

---

### 📱 Stage 4 — Reassembly on Your Phone

After all 71,820 TCP segments have arrived (possibly out of order, possibly with some retransmissions), your phone's network stack works bottom-up — the reverse of what the laptop did:

```
📡 Radio waves received by phone antenna
         │
         ▼
WiFi chip demodulates → binary bits (0s and 1s)
         │
         ▼
Frames assembled → FCS verified (corrupt frames discarded)
         │
         ▼
IP packets extracted → routing checked
         │
         ▼
TCP segments extracted → reordered by sequence number
         │
         ▼
HTTP response parsed → headers read, body extracted
         │
         ▼
File bytes written to phone storage (Flash memory)
         │
         ▼
✅ video.mp4 appears in your Downloads folder
```

The file bytes that come out at the bottom are **bit-for-bit identical** to what was on your laptop's disk. TCP + checksums guarantee this.

---

### 🔢 The Complete Journey — By the Numbers

For a **100 MB video file** download over WiFi:

```
Stat                              Value
──────────────────────────────────────────────────────────
File size on disk                 104,857,600 bytes
Total bits to transmit            838,860,800 bits
TCP segments created              ~71,820 segments
Bytes of TCP/IP overhead added    ~3.6 MB (headers)
WiFi symbols transmitted          ~104 million
WiFi radio frequency used         5 GHz (5,000,000,000 Hz)
Speed of radio waves              ~300,000 km/s
Time for signal to cross 10m room ~0.000000033 seconds
Typical transfer time (WiFi 5)    ~8–15 seconds
Bits that flip in transit         0 (TCP + FCS guarantee this)
```

---

### 🔐 Why Can't Someone Outside Your Home Intercept This?

Radio waves do travel through walls. But three things protect you:

**1. Local IP addresses** — Your router assigns your devices IPs like `192.168.1.x`. These are **private addresses** that are not routable on the public internet. Your file server is completely invisible outside your home network.

**2. Physical range** — WiFi at 5 GHz has a range of ~10–15 meters through walls. Someone in the street would receive a very weak signal.

**3. WPA2/WPA3 encryption** — Your WiFi password encrypts all data on the radio channel using AES-256. Even if someone captured the radio waves, they'd see encrypted garbage without your WiFi password.

---

### 🧩 Putting It All Together — The Full Picture

```
┌─────────────────────────────────────────────────────────────────────┐
│  YOUR LAPTOP                                                        │
│                                                                     │
│  video.mp4 on SSD                                                   │
│  [magnetic/electrical 0s and 1s]                                    │
│          │                                                          │
│          ▼                                                          │
│  OS reads file → bytes loaded into RAM (capacitor 0s and 1s)       │
│          │                                                          │
│          ▼                                                          │
│  Flask wraps bytes in HTTP response                                 │
│          │                                                          │
│          ▼                                                          │
│  TCP splits into 71,820 segments (adds port numbers, seq numbers)  │
│          │                                                          │
│          ▼                                                          │
│  IP wraps each segment (adds 192.168.1.10 → 192.168.1.25)         │
│          │                                                          │
│          ▼                                                          │
│  WiFi frame created (adds MAC addresses, FCS checksum)             │
│          │                                                          │
│          ▼                                                          │
│  WiFi chip: bits → 5 GHz radio waves (QAM modulation)             │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
                    📡 Radio waves travel at
                    speed of light (~3 ns for 1m)
                                │
              ┌─────────────────▼─────────────────┐
              │        WIFI ROUTER                │
              │  Acts as relay, forwards frames   │
              │  to the correct device by MAC     │
              └─────────────────┬─────────────────┘
                                │
                    📡 Radio waves continue
                                │
┌───────────────────────────────▼─────────────────────────────────────┐
│  YOUR PHONE                                                         │
│                                                                     │
│  WiFi chip antenna receives radio waves                             │
│          │                                                          │
│          ▼                                                          │
│  Demodulation: radio waves → 0s and 1s                             │
│          │                                                          │
│          ▼                                                          │
│  Frame check: FCS verified → corrupt frames dropped                │
│          │                                                          │
│          ▼                                                          │
│  TCP reassembly: segments put in order using sequence numbers      │
│          │                                                          │
│          ▼                                                          │
│  HTTP parsed: file bytes extracted from response body              │
│          │                                                          │
│          ▼                                                          │
│  Written to phone Flash storage (floating-gate transistors)        │
│          │                                                          │
│          ▼                                                          │
│  ✅ video.mp4 — identical bit-for-bit to what was on your laptop   │
└─────────────────────────────────────────────────────────────────────┘
```

> **The bottom line:** Your file never truly "moves." What happens is a process of **reading**, **encoding**, **transmitting**, **decoding**, and **writing** — the original 0s and 1s are faithfully **reproduced** on your phone through a chain of physics and protocols working in perfect harmony.

---

## 🔮 Roadmap

- [x] File size display on each card
- [x] QR code in terminal for easy mobile access
- [ ] Video preview / thumbnail
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