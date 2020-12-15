import smtplib, ssl
from email.message import EmailMessage

def mail(login_id, password, from_name, subject, message_body, mailer_list):

    with smtplib.SMTP_SSL(host ='smtp.gmail.com', port=465, context=ssl.create_default_context()) as server:
        server.login(login_id, password)
        email = EmailMessage()
        email['from'] = from_name
        email['subject'] = subject
        email.set_content(message_body)
        for i in mailer_list:
            email['to'] = i
            server.send_message(email)
            print('sent')
