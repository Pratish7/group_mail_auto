import smtplib, ssl
from smtplib import SMTPAuthenticationError
from email.message import EmailMessage
from tkinter import Tk, Label, Button

def mail(login_id, password, from_name, subject, message_body, mailers_list):

    status_window=Tk()

    status_label = Label(status_window, text = 'Sending')
    status_label.grid(row=0, column=0, padx=200, pady=25)

    ok_btn = Button(status_window, width=5, text='Ok', state='disabled')
    ok_btn.grid(row=1, column=0, pady=10)

    try:
        with smtplib.SMTP_SSL(host ='smtp.gmail.com', port=465, context=ssl.create_default_context()) as server:
            server.login(login_id, password)
            email = EmailMessage()
            email['from'] = from_name
            email['subject'] = subject
            email.set_content(message_body)
            email['to'] = mailers_list
            server.send_message(email)
            print('sent')
    except SMTPAuthenticationError:
        status_label.config(text='Authentication error\n'+'Please check your mail and password')
    
    finally:
        ok_btn.config(state='normal')

