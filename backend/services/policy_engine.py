def apply_policy(risk_level, options):
    action = "allowed"

    if options.get("block_high_risk") and risk_level in ["high", "critical"]:
        action = "blocked"
    elif options.get("mask"):
        action = "masked"

    return action