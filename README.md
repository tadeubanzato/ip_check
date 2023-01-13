## Dependencies
`pip3 install requests`

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
    sender_email = "email_sender@gmail.com"  # Enter your address
    receiver_email = "email_receiver@gmail.com"  # Enter receiver address
    password = "<< FROM ACCOUNT APP INFORMATION >>"

    msg = EmailMessage()
    msg.set_content(f'Hi,\n\nYour IP has been updated by your ISP.\nNew IP: {current_ip}\n\nRemember to update your Godaddy DNS')
    msg['Subject'] = 'ISP updated your IP'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email
```

## Cron Job
Cron is setup to run every 8 hours
```shell
0 */8 * * * cd python/ip_check/ && python3 get_ip.py
```
