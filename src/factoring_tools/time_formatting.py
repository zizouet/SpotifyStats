from datetime import datetime

def ms_to_hours(ms):
    """Convert milliseconds to hours.

    Args:
        ms (pandas df): data in ms

    Returns:
        pandas df: data in hours
    """
    return ms / 1000 / 60 / 60

def extract_hour_from_timestamp(timestamp):
    """Extract the hour from a timestamp.

    Args:
        timestamp (pandas df): array of timestamps

    Returns:
        pandas df: array of hours
    """
    # Parse the timestamp into a datetime object
    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    # Change to Local Time Zone
    dt = dt.astimezone()
    # Extract the hour
    hour = dt.hour
    return hour