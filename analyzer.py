print("=" * 45)
print("LOG FILE ANALYZER")
print("=" * 45)

failed_logins = 0
errors = 0
successful_logins = 0
suspicious_ips = []

with open("sample_log.txt", "r") as logfile:
    for line in logfile:

        if "Failed login" in line:
            failed_logins += 1

        if "logged in successfully" in line:
            successful_logins += 1

        if "ERROR" in line:
            errors += 1

        if "Connection from IP" in line:
            ip = line.split("IP")[1].strip()
            suspicious_ips.append(ip)

risk_score = failed_logins + errors

print("\nSecurity Summary")
print("----------------")
print(f"Successful Logins : {successful_logins}")
print(f"Failed Logins     : {failed_logins}")
print(f"Security Errors   : {errors}")

print("\nSuspicious IP Addresses")
print("-----------------------")

for ip in suspicious_ips:
    print("-", ip)

print(f"\nRisk Score: {risk_score}")

if risk_score >= 6:
    threat_level = "HIGH RISK"
elif risk_score >= 3:
    threat_level = "MEDIUM RISK"
else:
    threat_level = "LOW RISK"

print(threat_level)

if failed_logins >= 3:
    print("\nPossible Brute Force Attack Detected")

report = f"""LOG FILE ANALYSIS REPORT

Successful Logins : {successful_logins}
Failed Logins     : {failed_logins}
Security Errors   : {errors}

Suspicious IP Addresses
-----------------------
"""

for ip in suspicious_ips:
    report += f"{ip}\n"

report += f"""

Risk Score: {risk_score}
Threat Level: {threat_level}
"""

if failed_logins >= 3:
    report += "\nPossible Brute Force Attack Detected"

with open("reports/security_report.txt", "w") as file:
    file.write(report)

print("\nReport saved to reports/security_report.txt")