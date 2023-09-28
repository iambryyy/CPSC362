from twilio.rest import Client

account_sid = 'AC53136afc84d35948bf29c8cd8c7c9984'
auth_token = '2e9acbbdf904233ba29efa921e31fad2'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18447304514',
  body='Hello! You been added to contact book!',
  to='+17144958707'
)

print(message.sid)