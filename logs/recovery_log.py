import datetime

LOG_PATH = "logs/recovery_log.txt"

def log_recovery_event(description):
    """Append a recovery event with timestamp."""
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_PATH, "a") as file:
        file.write(f"[{timestamp}] RECOVERY: {description}\n")

def read_recovery_events():
    """Read all recovery events."""
    with open(LOG_PATH, "r") as file:
        return file.readlines()
