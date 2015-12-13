#!/usr/bin/python3
# lab12_example2.py
# send email from Python script using SMTP
# to RGU exchange server

import smtplib
import email.utils
from email.message import Message
from twython import Twython
import datetime

        

def sendTweet():
	
    credentials = open("./credentials/twitter_credentials.txt").read().splitlines()

    your_screen_name = "lef_kousis" #change this for your username

    # twitter credentials - edit yours here
    api_token = credentials[0]
    api_secret = credentials[1]
    access_token = credentials[2]
    access_token_secret = credentials[3]

    twitter=Twython(api_token, api_secret, access_token, access_token_secret)

    # send direct message, enter your Twitter screen name
    twitter.send_direct_message(\
        screen_name=your_screen_name, \
        text='Someone was the door at {}'.format(datetime.datetime.now()))

    # update status (uncomment if you wants status to be updated)
    # twitter.update_status(status='Hello from Python! CM2540 student at {}'.format(datetime.datetime.now()))

    print("Tweet sent")


# send email 

def sendEmail():
    credentials = open("./credentials/email_credentials.txt").read().splitlines() 
   
    to_email = credentials[0]
    servername = credentials[1]
    username = credentials[2]
    password = credentials[3]
    from_sender_name = credentials[4]
    from_sender_email = credentials[5]
    body = 'Someone was the door at {}'.format(datetime.datetime.now())
    subject = 'IR DETECT'
    
   
    
    # Create the message
    msg = Message()
    msg['To'] = email.utils.formataddr(('Recipient', to_email))
    msg['From'] = email.utils.formataddr((from_sender_name, from_sender_email))
    msg['Subject'] = subject
    msg['Date'] = email.utils.formatdate(localtime = 1)
    msg['Message-ID'] = email.utils.make_msgid()
    msg.set_payload(body)
    
    server = smtplib.SMTP(servername)
    try:
        # for verbose reporting
        server.set_debuglevel(False)
    
        # identify ourselves, prompting server for supported features
        server.ehlo_or_helo_if_needed()
    
        # If we can encrypt this session, do it
        if server.has_extn('STARTTLS'):
            server.starttls()
            # re-identify ourselves over TLS connection
            server.ehlo_or_helo_if_needed() 
    
        server.login(username, password)
        
        server.send_message(msg)
    finally:
        server.quit()
  