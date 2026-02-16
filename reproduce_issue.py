from twilio.rest import Client
import time
from datetime import datetime

# Setup Twilio account
account_sid = "AC990769cb8747c8a4fc4e0b1d2d58a7a0"
auth_token = "0960a5a7152eee8c1e8fd4e57a965b21"
client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message):
    print(f"Sending message to {recipient_number}...")
    try:
        message = client.messages.create(
            from_ = "whatsapp:+14155238886",
            body = message,
            to = f"whatsapp:{recipient_number}"
        )
        print(f"Message sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Hardcoded values for testing
name = "Test User"
recipient_number = "+1234567890" # Dummy number
message = "Test message from analysis"

print("Starting reproduction script...")
send_whatsapp_message(recipient_number, message)
print("Finished reproduction script.")
