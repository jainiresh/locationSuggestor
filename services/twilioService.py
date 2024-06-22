from twilio.rest import Client
from config.twilioCreds import twilioAccountSid, twilioAuthToken
import os

account_sid= os.getenv('twilioAccountSid', default=twilioAccountSid)
account_auth = os.getenv('twilioAuthToken', default=twilioAuthToken)
client = Client(account_sid, account_auth)

def createMessage(phoneNumber, content):
    try:
        print(f"sid : {twilioAccountSid} and auth : {twilioAuthToken}")
        message = client.messages.create(
            to='+91'+phoneNumber,
            from_="+19784044269",
            body=content)
        print(f"Message sent: {message} and {message}")
        return "ok"  # Return success message here if no exception occurs
    except Exception as e:
        print(f"An exception occurred: {e}")
        return "error"  # Return error message or handle as needed
