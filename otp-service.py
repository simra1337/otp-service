from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import random
from twilio.rest import Client
from dotenv import load_dotenv
import os
from flask import redirect
from flask import render_template
from datetime import datetime, timedelta

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('API_SECRET_KEY') # any random string

# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
db = SQLAlchemy(app)

class OTP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mobile_number = db.Column(db.String(20), nullable=False)
    otp = db.Column(db.String(6), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

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
    otp_object = OTP(mobile_number=mobile_number,otp=otp,expires_at=datetime.now() + timedelta(minutes=5))
    db.session.add(otp_object)
    db.session.commit()
    print(message.sid)
    return redirect('/otp')

@app.route('/otp/<otp>')
def handle_otp(otp):
    otp_data = OTP.query.filter_by(otp=otp).first()
    if otp_data:
        if datetime.now() < otp_data.expires_at:
            return "OTP is valid"
        else:
            #OTP.query.filter_by(otp=otp).delete()
            #db.session.commit()
            return "OTP has expired"
    else:
        return "Invalid OTP"

@app.route('/')
def open_index():
    return redirect('/homepage')

@app.route('/homepage')
def homepage():
    return render_template("send_otp.html")

@app.route('/otp')
def validate_otp_page():
    return render_template("validate_otp.html")

if __name__ == '__main__':
    app.run(debug=True)
