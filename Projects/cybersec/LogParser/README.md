# 📄 Log Parser

A lightweight Python-based log parser built to understand how security logs are processed and transformed into structured data.

This project focuses on parsing raw system logs into a format that can be easily analyzed by cybersecurity tools and analysts.

---

# 🚀 Features

* Reads log files line by line
* Parses Linux-style system logs
* Separates log headers from messages
* Extracts:

  * Timestamp
  * Hostname
  * Service
  * Message
* Returns structured Python dictionaries
* Modular project architecture

---

# 📂 Project Structure

```text
LogParser/
│
├── main.py              # Entry point
├── parser.py            # Log parsing logic
├── analyzer.py          # Reserved for future analysis
├── utils.py             # Helper functions
│
├── sample_logs/
│     └── sample.log
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🧠 How It Works

The parser processes logs using a simple pipeline.

```text
Log File
    │
    ▼
Read Line
    │
    ▼
Split Header & Message
    │
    ▼
Extract Fields
    │
    ▼
Return Dictionary
```

Each log entry is transformed from plain text into structured data.

Example input:

```text
Jun 28 12:01:10 kali sshd[2143]: Failed password for root from 192.168.1.10 port 55123 ssh2
```

Example output:

```python
{
    "timestamp": "Jun 28 12:01:10",
    "host": "kali",
    "service": "sshd[2143]",
    "message": "Failed password for root from 192.168.1.10 port 55123 ssh2"
}
```

---

# 🛠 Technologies Used

* Python 3
* File Handling
* String Parsing
* Dictionary Data Structures
* pathlib

---

# 📚 Concepts Learned

While building this project I learned:

* Reading files in Python
* Processing logs line by line
* String manipulation
* Using `split()`
* Using `partition()`
* Creating structured dictionaries
* Building modular Python applications

---

# ▶️ Running the Project

Clone the repository and navigate to the project directory.

Run:

```bash
python3 main.py
```

The parser will read the sample log file and print the structured output for each log entry.

---

# 📈 Future Improvements

* Regular Expression (Regex) support
* IP Address Extraction
* Username Extraction
* PID Extraction
* Authentication Status Detection
* JSON Export
* CSV Export
* Multi-format Log Support
* Integration with a Log Analyzer

---

# ⚠️ Disclaimer

This project is intended for educational purposes to understand log parsing techniques commonly used in cybersecurity, digital forensics, and incident response.

---

# 👨‍💻 Author

**Sreevatsa Rajesh**

Building cybersecurity tools from scratch to gain a deeper understanding of networking, operating systems, and defensive security.
