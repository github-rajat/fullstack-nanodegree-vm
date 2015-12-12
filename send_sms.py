from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3565e43df1ad216996dbafb915f74677"
auth_token  = "e647e6b95e1ced2ba8f2729cc2c0b657"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Voila!",
    to="+919560036156",    # Replace with your phone number
    from_="+12568875742") # Replace with your Twilio number
print message.sid                   
