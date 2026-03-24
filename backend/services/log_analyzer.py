from services.detector import detect_patterns

def analyze_logs(content):
    findings = []
    lines = content.split("\n")

    state = {
        "failed_login_count": 0
    }

    for i, line in enumerate(lines):
        line_findings = detect_patterns(line, i + 1, state)

        # attach actual log line
        for f in line_findings:
            f["content"] = line

        findings.extend(line_findings)

    return findings