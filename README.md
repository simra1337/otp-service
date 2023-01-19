## OTP Validation

This is a simple application that demonstrates how to send and validate an OTP (One-Time-Password) using Flask, Twilio, and JavaScript. 

## Features
- Generate a random OTP and send it via SMS using Twilio
- Validate the OTP for the provided mobile number
- OTP is valid for the specified time

## Requirements
- Twilio account and Twilio python library
- Flask
- Python 3.x
- .env file containing ACCOUNT_SID, AUTH_TOKEN and FROM phone number

## Getting Started

1. Clone the repository:
    git clone https://github.com/simra1337/otp-service.git


2. Install the required packages:
    pip install -r requirements.txt

3. Add your Twilio account SID and auth token to a `.env` file.

4. Run the application

5. To send the OTP to user, hit the url: http://localhost:5000

6. User will see message on the same page where user is validating the OTP.

Note: You can also use pythonanywhere or any other hosting service to host this application.

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Twilio](https://www.twilio.com/) - Used to send OTP via SMS
* [JavaScript](https://developer.mozilla.org/en-US/) - Used to handle form submission and display the message

## Note
- Make sure that you have the Twilio account and you have filled the ACCOUNT_SID, AUTH_TOKEN and FROM phone number in the .env file.
- Storing OTP in session is not secure, As session is stored in the browser, so it can be accessed by anyone. It is always better to use a database for storing the OTP and validate it.