# Install 'twilio' in order for the SMS notificaton feature to work: "pip install twilio"
# Importing Twilio
from twilio.rest import Client

account_sid = 'AC53136afc84d35948bf29c8cd8c7c9984' # Account SID || DO NOT CHANGE THIS
auth_token = '8dfd31773f5f10941c7a4ea4df3c675f'# Auth Token || DO NOT CHANGE THIS
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18447304514', # DO NOT CHANGE THIS
  body='Hello! You been added to contact book!', # edit body of message 
  to='+17144958707' # edit this with phone number(s) to send a text message as a notification
)

print(message.sid)