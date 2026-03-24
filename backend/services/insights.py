def generate_insights(findings):
    insights = []
    types = set(f["type"] for f in findings)

    if "password" in types:
        insights.append(
            "Critical: Plaintext passwords detected. This can lead to full account compromise."
        )

    if "api_key" in types:
        insights.append(
            "High Risk: API keys exposed. Attackers may gain unauthorized access to services."
        )

    if "stack_trace" in types:
        insights.append(
            "Medium Risk: Stack traces reveal internal system structure."
        )

    if "brute_force" in types:
        insights.append(
            "Suspicious Activity: Multiple failed login attempts detected (possible brute-force attack)."
        )

    if not insights:
        insights.append("No major threats detected. Logs appear safe.")

    return insights