from services.detector import detect_patterns
import re

# Proper IP regex
IP_REGEX = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

def analyze_logs(content):
    findings = []
    lines = content.split("\n")

    ip_count = {}
    failed_login_count = 0

    for i, line in enumerate(lines, start=1):

        # 🔍 Run pattern detection
        line_findings = detect_patterns(line, i)

        # 📌 Attach actual log line
        for f in line_findings:
            f["content"] = line

        findings.extend(line_findings)

        # 🔥 Track failed logins
        if "failed login" in line.lower():
            failed_login_count += 1

        # 🔥 Extract real IPs using regex
        matches = re.findall(IP_REGEX, line)
        for ip in matches:
            ip_count[ip] = ip_count.get(ip, 0) + 1

    # 🚨 Brute-force detection
    if failed_login_count >= 3:
        findings.append({
            "type": "brute_force",
            "risk": "critical",
            "line": "multiple"
        })

    # 🚨 Suspicious IP detection
    for ip, count in ip_count.items():
        if count >= 5:
            findings.append({
                "type": "suspicious_ip",
                "risk": "high",
                "line": "multiple",
                "ip": ip
            })

    return findings