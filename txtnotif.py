# Install 'twilio' in order for the SMS notificaton feature to work: "pip install twilio"
# * If you experience an error installing Twilio, visit this link and follow the steps in the video "https://www.youtube.com/watch?v=XFqaXaj8mm8"
# Importing Twilio
from twilio.rest import Client

account_sid = 'AC53136afc84d35948bf29c8cd8c7c9984' # Account SID || DO NOT CHANGE THIS
auth_token = '8dfd31773f5f10941c7a4ea4df3c675f'# Auth Token || DO NOT CHANGE THIS
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18447304514', # DO NOT CHANGE THIS
  body='Hello! You been added to contact book!', # edit body of message 
  to='+17148534531' # edit this with phone number(s) to send a text message as a notification
)

print(message.sid)