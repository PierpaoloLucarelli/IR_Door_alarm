#!/usr/bin/python3
# lab12_example2.py
# send email from Python script using SMTP
# to RGU exchange server

import smtplib
import email.utils
from email.message import Message


import datetime

        

def sendTweet():
    credentials = open("./credentials/twitter_credentials.txt").read().splitlines()

    your_screen_name = credentials[0]

    # twitter credentials - edit yours here
    api_token = credentials[1]
    api_secret = credentials[2]
    access_token = credentials[3]
    access_token_secret = credentials[4]

    twitter=Twython(api_token, api_secret, access_token, access_token_secret)

    # send direct message, enter your Twitter screen name
    twitter.send_direct_message(\
        screen_name=your_screen_name, \
        text="Another message sent at {}".format(datetime.datetime.now()))

    # update status
    twitter.update_status(status='Hello from Python! CM2540 student at {}'.format(datetime.datetime.now()))

    print("Tweet sent")


def sendEmail():
    credentials = open("./credentials/email_credentials.txt").read().splitlines()
   
    to_email = credentials[0]
    servername = credentials[1]
    username = credentials[2]
    password = credentials[3]
    from_sender_name = credentials[4]
    from_sender_email = credentials[5]
    body = 'Someone is at the door'
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
        server.set_debuglevel(True)
    
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
  