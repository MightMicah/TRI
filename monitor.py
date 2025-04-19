# monitor.py
import datetime
import os

# File paths
BREAK_LOG = "logs/break_log.txt"
RECOVERY_LOG = "logs/recovery_log.txt"
GROWTH_LOG = "logs/growth_log.txt"

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

def log_event(log_file, event):
    """Append an event with timestamp to a log file."""
    with open(log_file, "a") as f:
        timestamp = datetime.datetime.now().isoformat()
        f.write(f"[{timestamp}] {event}\n")

def break_event(description):
    """Log a break event."""
    log_event(BREAK_LOG, description)

def recovery_event(description):
    """Log a recovery event."""
    log_event(RECOVERY_LOG, description)

def growth_event(description):
    """Log a growth event."""
    log_event(GROWTH_LOG, description)

def main():
    print("=== Triplex Monitor ===")
    print("Select an event type:")
    print("1. Break")
    print("2. Recovery")
    print("3. Growth")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
    if choice == "1":
        desc = input("Describe the break: ")
        break_event(desc)
        print("Break event logged.")
    elif choice == "2":
        desc = input("Describe the recovery: ")
        recovery_event(desc)
        print("Recovery event logged.")
    elif choice == "3":
        desc = input("Describe the growth: ")
        growth_event(desc)
        print("Growth event logged.")
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
