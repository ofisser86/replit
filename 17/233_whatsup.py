from twilio.rest import Client
from sms_settings import AuthToken 
 
account_sid = 'ACaf78c9bf97e1905d27de74f89ba1982c' 
auth_token = AuthToken
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your Twilio code is 1238432',      
                              to='whatsapp:+380937282264' 
                          ) 
 
print(message.sid)