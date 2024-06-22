from twilio.rest import Client
from config.twilioCreds import twilioAccountSid, twilioAuthToken

client = Client(twilioAccountSid, twilioAuthToken)

def createMessage(phoneNumber, content):
    message = client.messages.create(
        to='+91'+phoneNumber,
        from_="19784044269",
        body=content
)
    return "ok"
