# IoT Credential Brute-Forcer 🔐

This project is a lightweight Python tool designed for **ethical hacking** and **penetration testing** of IoT and network devices using **default or weak credentials**. It scans your local network, identifies live hosts, and attempts brute-force logins over HTTP, SSH, and Telnet protocols using a known list of default usernames and passwords.

⚠️ **Educational Use Only**: This tool is for educational and authorized testing purposes only. Never use this tool against systems you do not own or have explicit permission to test.

---

## 📁 Project Structure

project/
├── bruteforce/
│ ├── credentials_loader.py
│ ├── http_bruteforce.py
│ ├── ssh_bruteforce.py
│ └── telnet_bruteforce.py
├── scanners/
│ ├── device_identifier.py
│ ├── network_scanner.py
│ └── port_scanner.py
├── defaults/
│ └── common_credentials.json
├── main.py
├── requirements.txt
└── README.md

---

## 🚀 Features

- **Network Scanning** (Linux only): Detect live hosts on your subnet.
- **Port Scanning**: Check for common ports (22, 23, 80, 443, etc.) on discovered devices.
- **Device Identification**: Attempt hostname resolution via reverse DNS.
- **Brute Force Attacks**:
  - **HTTP Form Auth**: Smart detection of successful logins via content, redirects, cookies.
  - **SSH**: Attempts logins using Paramiko.
  - **Telnet**: Uses telnetlib to try default credentials.
- **Credential List**: Loads common default credentials from a structured JSON file.

---

## ⚙️ Setup

### ✅ Requirements

- OS: **Linux** (for network scanning via `ip` and `ping`)
- Python: 3.6+
- Dependencies:
  - `requests`
  - `paramiko`

### 📦 Install

1. **Clone the repo**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/iot-bruteforcer.git
   cd iot-bruteforcer
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
3. **Run the tool**:
   ```bash
   python3 main.py

### 📘 How It Works

1. Discover Devices: Performs a ping sweep of the local subnet.
2. Scan Ports: Identifies open ports on each host.
3. Identify Device: Attempts to resolve the hostname.
4. Brute-Force Protocols:
  -HTTP: You will be prompted to enter the login field names (e.g., username, password).
  -SSH & Telnet: Uses default credentials from the provided list.

### 🔒 Notes

- Modular Design: Each brute-force module is independent and extendable.
- Custom Credential Lists: You can expand defaults/common_credentials.json with more usernames/passwords.
- Smart HTTP Brute: Compares login response with a baseline of failed attempts to infer successful login heuristically.

### 🧪 Disclaimer

This tool is for educational and ethical use only. Always ensure you have explicit permission before scanning or brute-forcing devices on any network. Unauthorized use of this software may be illegal in your jurisdiction.

---

Copyright (c) 2025 

Developed by Gui :p
If you found this useful, consider giving the project a ⭐ on GitHub!
