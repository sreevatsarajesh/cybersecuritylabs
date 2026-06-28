# 🔎 Port Scanner

A lightweight TCP port scanner written in Python to understand how port scanning works at the socket level.

This project was built from scratch as part of my cybersecurity learning journey, focusing on networking fundamentals rather than relying on existing scanning tools.

---

## 🚀 Features

* TCP Connect Scanning
* Open / Closed Port Detection
* Configurable Socket Timeout
* Banner Grabbing for Open Ports
* Common Service Identification
* Hostname Resolution
* Modular Project Structure

---

## 📂 Project Structure

```text
PortScanner/
│
├── main.py          # Entry point
├── scanner.py       # TCP port scanning logic
├── banner.py        # Banner grabbing
├── utils.py         # Helper functions & common ports
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🧠 How It Works

The scanner performs a TCP Connect Scan.

For every target port:

1. Creates a TCP socket.
2. Attempts a connection using `connect_ex()`.
3. Determines whether the port is open or closed.
4. Identifies the commonly associated service.
5. Attempts to retrieve a service banner if available.

Workflow:

```text
Target Host
      │
      ▼
Resolve Hostname
      │
      ▼
Create TCP Socket
      │
      ▼
Attempt Connection
      │
      ├──────── Closed
      │
      └──────── Open
                  │
                  ▼
          Identify Service
                  │
                  ▼
            Grab Banner
```

---

## 🛠 Technologies Used

* Python 3
* Socket Programming
* TCP/IP Networking
* Git

---

## 📚 Concepts Learned

While building this project I learned:

* TCP Socket Programming
* TCP Three-Way Handshake
* `connect()` vs `connect_ex()`
* Port States
* Socket Timeouts
* Service Enumeration
* Banner Grabbing
* Modular Software Design

---

## ▶️ Running the Project

Edit the target host and port list in `main.py`, then run:

```bash
python3 main.py
```

Example output:

```text
22    OPEN     SSH
80    OPEN     HTTP
443   OPEN     HTTPS
```

---

## 📈 Future Improvements

* Command-line arguments
* Range scanning
* Concurrent scanning using ThreadPoolExecutor
* JSON output
* CSV export
* Better exception handling
* Progress indicator
* Colored terminal output

---

## ⚠️ Disclaimer

This project is intended for educational purposes and should only be used to scan systems that you own or have explicit permission to test.

---

## 👨‍💻 Author

**Sreevatsa Rajesh**

Building cybersecurity tools from scratch to develop a deeper understanding of computer networks, security, and systems programming.
