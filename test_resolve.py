import socket
import sys

hostname = 'api.twilio.com'
print(f"Attempting to resolve {hostname}...")
try:
    info = socket.getaddrinfo(hostname, 443)
    print(f"Successfully resolved {hostname}:")
    for res in info:
        print(res)
except Exception as e:
    print(f"Failed to resolve {hostname}: {e}")
    sys.exit(1)
