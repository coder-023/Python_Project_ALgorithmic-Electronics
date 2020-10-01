import smtplib,ssl
from twilio.rest import Client
def email_send():
    smtp_server="smtp.gmail.com"
    sender_email=""                                  #enter sender mail id
    receiver_email=""                                #enter receiver mail id
    port=465
    password=''                                      #enter password of account through which you wanna send
    message="""
    Subject:Voialation of Social Distancing
    Respected Sir,
          This is a mail to inform you that the social distancing is being hampered in lift.
    """
    context=ssl.create_default_context()
    server=smtplib.SMTP_SSL(smtp_server,port,context=context)
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message)
    
def send_message():
    account_sid = ''                               #enter account SID from twilio console
    auth_token = ''                                #enter token from your twilio console               
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="Social Distancing is hampered.Please have a look!",
                     from_='',                     #copy paste this from twilio 
                     to=''                         #enter verified phone number to whom you wanna send
                 )

    #print(message.sid)
        
