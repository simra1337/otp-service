import random
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Generate a random OTP
otp = random.randint(100000, 999999)

# Send the OTP via SMS
message = client.messages.create(
    body='Your OTP is: ' + str(otp),
    from_=os.environ.get('FROM'),
    to=os.environ.get('TO')
)

print(message.sid)