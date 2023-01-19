from flask import Flask, session
import random
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('API_SECRET_KEY') # any random string

# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token)

@app.route('/sendOtp/<mobile_number>')
def send_otp(mobile_number):
    # Generate a random OTP
    otp = random.randint(100000, 999999)
    # Send the OTP via SMS
    message = client.messages.create(
        body='Your OTP is: ' + str(otp),
        from_=os.environ.get('FROM'),
        to='+91' + mobile_number
    )
    session["mobile_number"] = mobile_number
    session["otp"] = otp
    print(message.sid)
    return "OTP sent to {}".format(mobile_number)

@app.route('/otp/<otp>')
def handle_otp(otp):
    # get the mobile number from session
    mobile_number = session.get("mobile_number")
    # get the otp from session
    stored_otp = session.get("otp")

    if stored_otp:
        if stored_otp == int(otp):
            return "Valid otp"
            # OTP is valid
            # Perform desired action
            pass
        else:
            return "Invalid otp"
            # OTP is invalid
            pass
    else:
        return "Otp Expired"
        pass


if __name__ == '__main__':
    app.run(debug=True)
