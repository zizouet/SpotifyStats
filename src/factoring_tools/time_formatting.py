from datetime import datetime

def ms_to_hours(ms):
    """
    Convert milliseconds to hours.
    """
    return ms / 1000 / 60 / 60

def extract_hour_from_timestamp(timestamp):
    # Parse the timestamp into a datetime object
    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    # Change to Local Time Zone
    dt = dt.astimezone()
    # Extract the hour
    hour = dt.hour
    return hour