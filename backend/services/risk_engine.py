def calculate_risk(findings):
    score = 0

    weights = {
        "critical": 5,
        "high": 3,
        "medium": 2,
        "low": 1
    }

    for f in findings:
        score += weights.get(f["risk"], 0)

    if score >= 10:
        level = "critical"
    elif score >= 7:
        level = "high"
    elif score >= 4:
        level = "medium"
    else:
        level = "low"

    return score, level