def generate_insights(findings):
    insights = []

    types = [f["type"] for f in findings]

    if "password" in types:
        insights.append("Critical: Plaintext passwords detected. Risk of account compromise.")

    if "api_key" in types:
        insights.append("High Risk: API keys exposed. Unauthorized access possible.")

    if "stack_trace" in types:
        insights.append("Medium Risk: Stack traces reveal internal system structure.")

    if "brute_force" in types:
        insights.append("Alert: Multiple failed login attempts detected.")

    if "ip_address" in types:
        insights.append("Info: IP addresses found in logs.")

    if not insights:
        insights.append("No major threats detected. Logs appear safe.")

    return insights