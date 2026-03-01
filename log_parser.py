import re

def parse_logs(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    error = 0
    warning = 0
    critical = 0

    for line in lines:
        if "ERROR" in line:
            error += 1
        if "WARNING" in line:
            warning += 1
        if "CRITICAL" in line:
            critical += 1

    logs_per_minute = len(lines) / 5  

    return [error, warning, critical, logs_per_minute]