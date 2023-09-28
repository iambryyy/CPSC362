from twilio.rest import Client

account_sid = 'AC53136afc84d35948bf29c8cd8c7c9984'
auth_token = '8dfd31773f5f10941c7a4ea4df3c675f'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18447304514',
  body='Hello! You been added to contact book!',
  to='+17144958707'
)

print(message.sid)