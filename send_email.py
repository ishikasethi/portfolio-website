import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "ishikasethi2806@gmail.com"
    password = "qrkuzdzetfkknzgt"
    receiver = "ishikasethi2806@gmail.com"
    context = ssl.create_default_context()

    print(username)
    print(password)
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

# send_email()
