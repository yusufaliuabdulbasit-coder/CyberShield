# 🛡️ CyberShield

**CyberShield** is a Django-based cybersecurity web application designed to provide a simple interface for network scanning and security exploration.

## About the Project

CyberShield integrates the Nmap network scanning tool with a Django web application. It allows users to submit an IP address and view scan results through a web interface.

The project is being developed as a practical cybersecurity learning project.

## Features

- **Web Dashboard:** A homepage providing access to the application's functionality.
- **Network Scanner:** Performs network scans using Nmap.
- **IP Validation:** Checks submitted IP addresses using Python's `ipaddress` module.
- **TCP Connect Scanning:** Uses Nmap's `-sT` option.
- **Port Scanning:** Scans the top 20 ports.
- **Error Handling:** Provides feedback for invalid IP addresses and unsuccessful scans.
- **Timeout Protection:** Limits scan execution time.

## Technologies Used

- Python
- Django
- Nmap
- HTML
- CSS
- Linux / Parrot OS

## Project Structure

```text
CyberShield/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── dashboard/
│   ├── templates/
│   │   └── dashboard/
│   │       └── index.html
│   ├── static/
│   ├── views.py
│   └── urls.py
│
├── customers/
│
├── scanner/
│   ├── templates/
│   │   └── scanner/
│   │       └── index.html
│   ├── views.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone git@github.com:yusufaliuabdulbasit-coder/CyberShield.git
cd CyberShield
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Nmap

On Parrot OS or Debian-based Linux:

```bash
sudo apt update
sudo apt install nmap
```

### 6. Run database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application at:

`http://127.0.0.1:8000/`

## Security and Responsible Use

CyberShield is intended for educational purposes and authorized security testing.

Only scan IP addresses and networks that you own or have explicit permission to assess. Unauthorized network scanning may violate applicable laws and policies.

## Developer

**Yusuf Basit**

Cybersecurity Student | Aspiring Security Professional

GitHub: [@yusufaliuabdulbasit-coder](https://github.com/yusufaliuabdulbasit-coder)

---

*CyberShield — Exploring Network Security Through Practical Learning.*
