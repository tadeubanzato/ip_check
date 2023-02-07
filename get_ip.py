#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# get_ip.py

from requests import get
import json
import time
from datetime import datetime
from dotenv import load_dotenv
from modules.update_godaddy import *
from modules.email import *
import os

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

        send_mail(current_ip)
        # godaddy(current_ip)

        with open('ip_info.json', 'w', encoding = 'utf-8') as f:
            json.dump(data, f, ensure_ascii = False, indent = 4)

    else:
        print('IP still the same')
