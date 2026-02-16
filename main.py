#step 1 install required libaries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

#step 2 set up twilio account
account_sid = "AC990769cb8747c8a4fc4e0b1d2d58a7a0"
auth_token = "0960a5a7152eee8c1e8fd4e57a965b21"
client = Client(account_sid, auth_token)

#step 3 define function to send whatsapp message
def send_whatsapp_message(recipient_number, message):
    try:
        message = client.messages.create(
            from_ = "whatsapp:+14155238886",
            body = message,
            to = f"whatsapp:{recipient_number}"
        )
        print(f"Message sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Error sending message: {e}")

#step 4
name = input("Enter the recepient name: ")
recipient_number = input("Enter the recepient whatsapp number with contry code(eg, +12345)")
message = input(f"enter the message you want to send to {name}")

#step 5 parse data/time  and calculate delay
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24hour format): ")

#date time
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <=0:
    print('the specified time is the past. Please enter future date and time')
else:
    print(f'Message schedule to be sent to {name} at {schedule_datetime}.')

    #wait untill the schedule time
    time.sleep(delay_seconds) 

    #send the message
    send_whatsapp_message(recipient_number,message)


