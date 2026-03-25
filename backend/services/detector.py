from backend.utils.patterns import EMAIL_PATTERN, API_KEY_PATTERN, PASSWORD_PATTERN, IP_PATTERN

failed_attempts = 0
ip_counter = {}

def detect_patterns(line, line_number):
    global failed_attempts
    findings = []

    line_lower = line.lower()

    if EMAIL_PATTERN.search(line):
        findings.append({"type": "email", "risk": "low", "line": line_number})

    if PASSWORD_PATTERN.search(line):
        findings.append({"type": "password", "risk": "critical", "line": line_number})

    if API_KEY_PATTERN.search(line):
        findings.append({"type": "api_key", "risk": "high", "line": line_number})

    if "error" in line_lower:
        findings.append({"type": "stack_trace", "risk": "medium", "line": line_number})

    if "failed login" in line_lower:
        failed_attempts += 1
        if failed_attempts >= 3:
            findings.append({"type": "brute_force", "risk": "high", "line": line_number})

    ip_match = IP_PATTERN.search(line)
    if ip_match:
        ip = ip_match.group()
        ip_counter[ip] = ip_counter.get(ip, 0) + 1

        findings.append({"type": "ip_address", "risk": "low", "line": line_number})

        if ip_counter[ip] > 3:
            findings.append({"type": "suspicious_ip", "risk": "high", "line": line_number})

    return findings