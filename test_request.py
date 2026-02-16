import requests
import sys

url = 'https://api.twilio.com'
print(f"Attempting GET request to {url}...")
try:
    response = requests.get(url, timeout=10)
    print(f"Response status code: {response.status_code}")
    print("Successfully connected.")
except requests.exceptions.RequestException as e:
    print(f"Failed to connect to {url}: {e}")
    sys.exit(1)
