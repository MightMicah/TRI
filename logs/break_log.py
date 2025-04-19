import datetime

LOG_PATH = "logs/break_log.txt"

def log_break_event(description):
    """Append a break event with timestamp."""
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_PATH, "a") as file:
        file.write(f"[{timestamp}] BREAK: {description}\n")

def read_break_events():
    """Read all break events."""
    with open(LOG_PATH, "r") as file:
        return file.readlines()
