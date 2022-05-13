from email import message
import smtplib
from email.mime.text import MIMEText #allows us to send text and html emails
from dotenv import load_dotenv
import os

load_dotenv()

def send_confirmation(user):
    port = 2525
    smtplib_server = 'smtp.mailtrap.io'
    login = os.environ.get("MAIL_LOGIN")
    password = os.environ.get("MAIL_PWRD")
    message = f"<h3> New user registered</h3>.Their name is {user}"
    sender_email = 'christinekrm02@gmail.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'New user registration'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    with smtplib.SMTP(smtplib_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

