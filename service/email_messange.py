"""
    Service for sending emails
"""

from smtplib import SMTP, SMTPException
from email.mime.text import MIMEText
from config.config import APP_EMAIL, APP_EMAIL_PASSWORD

def send_email(subject, message):
    """sending emails"""

    sender = APP_EMAIL
    password = APP_EMAIL_PASSWORD

    server = SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = subject
        server.sendmail(sender,sender,msg.as_string())

        return True
    except SMTPException as error:
        raise f'{error}\nChek your login or password please!'
