#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# get_ip.py

from requests import get
import json
import smtplib, ssl
from email.message import EmailMessage
import time
from datetime import datetime
import os
from dotenv import load_dotenv
from modules.update_godaddy import *

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

def ip_check():
    # data['ip-info']['old'] = get('https://api.ipify.org').content.decode('utf8')
    ip_now = get('https://api.ipify.org').content.decode('utf8')
    return ip_now


if __name__ == '__main__':

    load_dotenv()
    current_ip = ip_check()

    f = open('ip_info.json')
    data = json.load(f)

    ## Check if old and new ips are the different
    if data['ip-info']['latest'] != current_ip:
        print('IP was updated by ISP')
        data['ip-info']['latest'] = current_ip
        data['ip-info']['timestamp'] = time.time()
        data['ip-info']['date'] = str(datetime.fromtimestamp(time.time()))

        with open('ip_info.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        send_mail(current_ip)
        godaddy()
    else:
        print('IP still the same')
