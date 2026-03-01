def calculate_risk(features, anomaly):
    error, warning, critical, _ = features

    if critical > 0:
        return "HIGH"
    elif anomaly == -1:
        return "MEDIUM"
    else:
        return "LOW"