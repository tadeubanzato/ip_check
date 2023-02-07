#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# email.py

import os
import smtplib, ssl
from email.message import EmailMessage

"""
To enable email delivery go to the following link:
https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4O9FsLO4KIpWFl7veDJgjyfNA-2rPxmvgVm9E5NnlcK3kogsLF99FlMeGHUXDVorvZVuC1gYpsZR3mSk8Oy5CXqG7g9UA
Under security and generate the 2FA code for the API
"""

def send_mail(current_ip):
    port = 465  # For SSL
    smtp_server = 'smtp.gmail.com'
    password = os.environ.get('gmail_pass')
    sender_email = os.environ.get('from_email')
    receiver_email = os.environ.get("to_email").split(',') #['8577075969@tmomail.net', 'tadeubanzato@gmail.com']

    msg = EmailMessage()
    msg.set_content(f'Hi,\n\nYour IP has been updated by your ISP.\nNew IP: {current_ip}\n\nRemember to update your Godaddy DNS')
    msg['Subject'] = 'ISP updated your IP'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)