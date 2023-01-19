## Dependencies
This repository uses Python3 and Requests to get the current WAN IP data.
Install requests using the command `pip3 install requests`

## Dotenv for credentials
I also added a DOTENV adition to script so I do not share my current credentials live.
Refer to `.env-sample` file in the repository but essentially this file contains the emails information and the password acquired from the link below on Email Delivery session below.

```
from_email = sender-email@gmail.com
to_email = receiver-email@gmail.com
gmail_pass = <<PASS FROM GOOGLE>>

```

> Don't forget to change the `.env-sample` file name to `.env` only or create another file called `.env`

## JSON Swagger

```json
{
    "ip-info": {
        "latest": "1.2.3.4",
        "timestamp": 1673244266.359345,
        "date": "2023-01-08 22:04:26.359351"
    }
}
```
## Email delivery
Email SMTP is from Google using the appropriate credentials.
Need to add a new login/app into Google account catalog at:
https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4O9FsLO4KIpWFl7veDJgjyfNA-2rPxmvgVm9E5NnlcK3kogsLF99FlMeGHUXDVorvZVuC1gYpsZR3mSk8Oy5CXqG7g9UA

### Send email function
```python
def send_mail(current_ip):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    password = os.environ.get("gmail_pass")

    msg = EmailMessage()
    msg.set_content(f'Hi,\n\nYour IP has been updated by your ISP.\nNew IP: {current_ip}\n\nRemember to update your Godaddy DNS')
    msg['Subject'] = 'ISP updated your IP'
    msg['From'] = os.environ.get('from_email')
    msg['To'] = os.environ.get('to_email')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)
```

## Cron Job
Cron is setup to run every 8 hours
```shell
0 */8 * * * cd python/ip_check/ && python3 get_ip.py
```
