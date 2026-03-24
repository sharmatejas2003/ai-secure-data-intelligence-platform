def generate_insights(findings):
    insights = []
    types = [f["type"] for f in findings]

    if "password" in types:
        insights.append("🚨 Critical: Plaintext passwords detected. Immediate action required.")

    if "api_key" in types:
        insights.append("🔐 API keys exposed. This may lead to unauthorized access.")

    if "stack_trace" in types:
        insights.append("⚠️ Stack traces reveal internal system architecture.")

    if "brute_force" in types:
        insights.append("🚨 Multiple failed login attempts detected (possible brute-force attack).")

    if "ip_address" in types:
        insights.append("🌐 Multiple IP addresses found. Check for suspicious activity.")

    if not insights:
        insights.append("✅ No major threats detected. Logs appear safe.")

    return insights