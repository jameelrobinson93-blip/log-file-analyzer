# Log File Analyzer

## Overview

The Log File Analyzer is a Python application that analyzes security log files for suspicious activity.

The program detects failed login attempts, successful logins, malware events, suspicious IP addresses, and potential brute-force attacks. It generates a security report that can be used for security monitoring and incident response.

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
- String Parsing
- Lists
- Loops
- Conditional Statements

---

## Project Structure

```
log-file-analyzer/
│
├── analyzer.py
├── sample_log.txt
├── requirements.txt
├── README.md
│
├── reports/
│   └── security_report.txt
│
└── screenshots/
```

---

## Example Output

```
LOG FILE ANALYZER
=============================================

Successful Logins : 2
Failed Logins     : 4
Errors            : 3

Suspicious IP Addresses
-----------------------
185.200.118.15
45.67.89.22

Risk Score: 7

Threat Level: HIGH RISK

Possible Brute Force Attack Detected
```

---

## Generated Report

After running the analyzer, a report is automatically created inside:

```
reports/security_report.txt
```

---

## Future Improvements

- Export reports as CSV
- Export reports as JSON
- Add command-line arguments
- Create a graphical user interface (GUI)
- Integrate VirusTotal API
- Add IP geolocation lookup
- Detect additional attack patterns

---

## Author

**Jameel Robinson**

Aspiring SOC Analyst | Python | Cybersecurity | GitHub Portfolio
