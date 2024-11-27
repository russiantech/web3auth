from os import getenv
from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from web import mail

def send_async_email(app, msg):
    try:
        with app.app_context():
            mail.send(msg)
            print(f'sucess, email sent {msg}!')
    except Exception as e:
        print(f'Email-failed ->{e} | {getenv("MAIL_USERNAME")}, {getenv("MAIL_PASSWORD") } ')

def send_email_former_async(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = html_body
    msg.body = text_body
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    try:
        with current_app.app_context():
            mail.send(msg)
            print(f"Email sent successfully to {recipients}")
    except Exception as e:
        print(f"Error sending email: {e} | Sender: {sender}, Recipients: {recipients}")


def reset_email(user):
    token = user.generate_token(type='reset')
    send_email(
        ('[Russiantechnologies] . Reset Your Password'),
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[user.email],
        text_body=render_template('email/forgot.txt', user=user, token=token),
        html_body=render_template('email/forgot.html', user=user, token=token)
               )

def verify_email(user):
    token = user.generate_token(exp=86400, type='verify')
    send_email(
        ('[Russiantechnologies] . Verifications'),
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[user.email],
        text_body=render_template('email/verify.txt', user=user, token=token),
        html_body=render_template('email/verify.html', user=user, token=token)
               )

