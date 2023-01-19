# OTP Generator and Validator

This script is used to generate and validate OTPs using Twilio.

## Features
- Generate a random OTP and send it via SMS using Twilio
- Validate the OTP for the provided mobile number
- OTP is valid for the specified time

## Requirements
- Twilio account and Twilio python library
- Flask
- Python 3.x
- .env file containing ACCOUNT_SID, AUTH_TOKEN and FROM phone number

## Usage
1. Install the required packages by running `pip install -r requirements.txt`
2. Run the script with `python otp-service.py`
3. To send the OTP, navigate to `http://localhost:5000/sendOtp/{mobile_number}` in your browser
4. To validate the OTP, navigate to `http://localhost:5000/otp/{otp}` in your browser

## Note
- Make sure that you have the Twilio account and you have filled the ACCOUNT_SID, AUTH_TOKEN and FROM phone number in the .env file.
- Storing OTP in session is not secure, As session is stored in the browser, so it can be accessed by anyone. It is always better to use a database for storing the OTP and validate it.
