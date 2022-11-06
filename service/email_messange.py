"""
    Service for sending emails
"""

from smtplib import SMTP, SMTPException
from email.mime.text import MIMEText
from config.config import APP_EMAIL, APP_EMAIL_PASSWORD


def send_email(email, sample_html, subject):
    """sending emails"""

    sender = APP_EMAIL
    password = APP_EMAIL_PASSWORD

    server = SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(sample_html, "html")
        msg['From'] = sender
        msg['To'] = email
        msg['Subject'] = subject
        server.sendmail(sender, email, msg.as_string())

        return True
    except SMTPException as error:
        raise f'{error}\nChek your login or password please!'


def activate_email(email, username, coding):
    """
        Sending a message to activate the user's email
    """
    try:
        with open("./html/activaite_email.html", encoding='utf-8') as file:
            temap = file.read()
    except IOError as err:
        raise f'{err}\nFailed to open template'

    temap = temap.replace('#username#', username)
    temap = temap.replace('#activation_key#', coding)

    send_email(
        email,
        temap,
        f'Hello {username} ! Welcome to MyBlog!'
    )


def password_recovery(email, username, coding):
    """
        Sending a message to recovery password
    """
    try:
        with open("./html/recovery_password.html", encoding='utf-8') as file:
            temap = file.read()
    except IOError as err:
        raise f'{err}\nFailed to open template'

    temap = temap.replace('#username#', username)
    temap = temap.replace('#confirmation#', coding)

    send_email(
        email,
        temap,
        f'Hello {username}! Have you forgotten your password?'
    )
