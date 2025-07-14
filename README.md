# 📡 Bluetooth Attendance Tracking System

This project tracks student attendance by scanning for Bluetooth MAC addresses. It's useful for small group environments like hostels or classrooms where students carry registered Bluetooth-enabled devices.

---

## 📁 Project Structure

bluetooth_attendance/
│
├── main.py
├── requirements.txt
├── README.md
├── venv/ # (virtual environment)
├── data/
│ └── students.csv # MAC to name mapping
├── output/
│ └── attendance_YYYY-MM-DD.csv # Automatically generated
└── attendance/
  └── __init__.py
  └── scanner.py
  └── attendance.py
  └── csv_handler.py

---

## 🧑‍💻 Setup Instructions

### 1️⃣  Clone or Download the Project
        ```bash
        git clone https://github.com/yourusername/bluetooth_attendance.git
        cd bluetooth_attendance

### 2️⃣  Create and Activate Virtual Environment
        python3 -m venv venv

        - Linux/macOS:
            ```bash
            source venv/bin/activate
        - Windows CMD:
            ```bash
            venv\Scripts\activate
        - Windows PowerShell:
            ```bash
            .\venv\Scripts\Activate.ps1

### 3️⃣  Install Dependencies
        pip install -r requirements.txt


### 4️⃣  Add Student Data
        Create a CSV file: `data/students.csv` in the format:
        ```bash
        MAC,Name
        f8:ad:24:99:71:40,Hari
        A8:05:56:1C:DE:86,Vinod
        5C:A0:6C:6B:F2:6A,NagaTeja

### 5️⃣  Run the Application
        ```bash
        python main.py
## Features
    - Bluetooth scanning using PyBluez.
    - Automatic detection of students by MAC address.
    - Attendance logs with timestamps.
    - CSV export with present/absent status.

## Note
    - Make sure your device’s Bluetooth is enabled and discoverable.
    - This script must be run on a system with Bluetooth support (e.g., Raspberry Pi, Linux/Mac laptops).

## License
    This project is open-source. Feel free to use and adapt it.

---
