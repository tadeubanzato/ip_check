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