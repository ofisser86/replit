from twilio.rest import Client
from sms_settings import AuthToken 
 
account_sid = 'ACaf78c9bf97e1905d27de74f89ba1982c' 
auth_token = AuthToken
client = Client(account_sid, auth_token) 
msg = 'Python twilio mssg'
message = client.messages.create( 
                              from_='+12093967386',
                              body=msg,        
                              to='+380937282264' 
                          ) 
 
print(message.sid)