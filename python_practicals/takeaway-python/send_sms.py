import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC036e7433091baff14fc3efdca822662c'
auth_token = '681e8dfca4891bb27beb751d4371b9b8'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='[+][44][7480318797]',
                     to='[+][44][7480318797]'
                 )

print(message.sid)
