def get_risk_color(risk):
    if risk == "critical":
        return "red"
    elif risk == "high":
        return "orange"
    elif risk == "medium":
        return "yellow"
    else:
        return "green"