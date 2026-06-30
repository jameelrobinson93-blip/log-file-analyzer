# Log File Analyzer

## Overview

The Log File Analyzer is a Python application that analyzes security log files for suspicious activity.

The program detects failed login attempts, successful logins, malware events, suspicious IP addresses, and possible brute-force attacks. It automatically generates a security report that can be used for security monitoring and incident response.

---

## Features

- Analyze security log files
- Detect failed login attempts
- Count successful logins
- Detect malware events
- Extract suspicious IP addresses
- Calculate a security risk score
- Detect possible brute-force attacks
- Automatically generate a security report

---

## Technologies Used

- Python 3
- File Handling
- String Processing
- Git
- GitHub
- Visual Studio Code

---

## Installation

Clone the repository:

```bash
git clone https://github.com/jameelrobinson93-blip/log-file-analyzer.git
```

Navigate into the project folder:

```bash
cd log-file-analyzer
```

Run the application:

```bash
python analyzer.py
```

---

## Project Structure

```
log-file-analyzer/
│
├── analyzer.py
├── sample_log.txt
├── requirements.txt
├── README.md
├── reports/
│   └── security_report.txt
└── screenshots/
    ├── project_structure.png
    ├── terminal_output.png
    └── security_report.png
```

---

## Sample Log File

The included `sample_log.txt` contains examples of:

- Successful user logins
- Failed login attempts
- Malware detection
- Suspicious IP connections
- Security errors

---

## Sample Output

```
=============================================
LOG FILE ANALYZER
=============================================

Security Summary
----------------

Successful Logins : 2
Failed Logins     : 4
Security Errors   : 3

Suspicious IP Addresses
-----------------------

185.200.118.15
45.67.89.22

Risk Score: 7

HIGH RISK

Possible Brute Force Attack Detected

Report saved to reports/security_report.txt
```

---

## Generated Report

After running the analyzer, a report is automatically created inside:

```
reports/security_report.txt
```

Example report contents:

```
LOG FILE ANALYSIS REPORT

Successful Logins : 2
Failed Logins     : 4
Security Errors   : 3

Suspicious IP Addresses

185.200.118.15
45.67.89.22

Risk Score: 7
Threat Level: HIGH RISK

Possible Brute Force Attack Detected
```

---

## Screenshots

Project screenshots are stored in the **screenshots** folder and include:

- Project folder structure
- Terminal output after running the analyzer
- Generated security report

---

## Future Improvements

- Export reports as CSV
- Export reports as JSON
- Add command-line arguments
- Create a graphical user interface (GUI)
- Integrate VirusTotal API
- Add IP geolocation lookup
- Detect additional attack patterns
- Support multiple log file formats

---

## Skills Demonstrated

- Python Programming
- Cybersecurity Fundamentals
- Log Analysis
- Threat Detection
- File Processing
- Risk Assessment
- Git Version Control
- GitHub Project Management

---

## Author

**Jameel Robinson**

Cybersecurity Portfolio Project

GitHub:
https://github.com/jameelrobinson93-blip
