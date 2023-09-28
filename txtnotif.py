from twilio.rest import Client

account_sid = 'AC53136afc84d35948bf29c8cd8c7c9984' # DO NOT CHANGE THIS
auth_token = '8dfd31773f5f10941c7a4ea4df3c675f'# DO NOT CHANGE THIS
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18447304514', # DO NOT CHANGE THIS
  body='Hello! You been added to contact book!', # edit body of message 
  to='+17144958707' # edit this with a phone number to send a text message to
)

print(message.sid)