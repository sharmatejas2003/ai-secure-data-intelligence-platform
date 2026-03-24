from utils.patterns import EMAIL_PATTERN, API_KEY_PATTERN, PASSWORD_PATTERN, IP_PATTERN

def detect_patterns(line, line_number, state):
    findings = []

    # EMAIL
    if EMAIL_PATTERN.search(line):
        findings.append({
            "type": "email",
            "risk": "low",
            "line": line_number
        })

    # PASSWORD
    if PASSWORD_PATTERN.search(line):
        findings.append({
            "type": "password",
            "risk": "critical",
            "line": line_number
        })

    # API KEY
    if API_KEY_PATTERN.search(line):
        findings.append({
            "type": "api_key",
            "risk": "high",
            "line": line_number
        })

    # STACK TRACE / ERROR
    if "ERROR" in line:
        findings.append({
            "type": "stack_trace",
            "risk": "medium",
            "line": line_number
        })

    # FAILED LOGIN TRACKING (SMART WAY)
    if "failed login" in line.lower():
        state["failed_login_count"] += 1

        if state["failed_login_count"] >= 3:
            findings.append({
                "type": "brute_force",
                "risk": "high",
                "line": line_number
            })

    # IP DETECTION
    if IP_PATTERN.search(line):
        findings.append({
            "type": "ip_address",
            "risk": "low",
            "line": line_number
        })

    return findings