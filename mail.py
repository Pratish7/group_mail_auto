import smtplib, ssl
from smtplib import SMTPAuthenticationError
from email.message import EmailMessage
from tkinter import Tk, Label, Button



def mail(login_id, password, from_name, subject, message_body, mailers_list):

    global status_window
    status_window=Tk()
    status_window.title('Status')

    status_label = Label(status_window, text = 'Sending')
    status_label.grid(row=0, column=0, padx=200, pady=25)

    ok_btn = Button(status_window, width=5, text='Ok', state='disabled', command=ok_command)
    ok_btn.grid(row=1, column=0, pady=10)

    for i in mailers_list:
        try:
            with smtplib.SMTP_SSL(host ='sg3plcpnl0152.prod.sin3.secureserver.net', port=465, context=ssl.create_default_context()) as server:
                status_label.config(text='sending to '+i)
                server.login(login_id, password)
                email = EmailMessage()
                email['from'] = login_id
                email['subject'] = subject
                email.set_content(message_body)
                email['to'] = i
                server.send_message(email)
        except SMTPAuthenticationError:
            status_label.config(text='Authentication error\n'+'Please check your mail and password')
    
    status_label.config(text='Sent')    
    ok_btn.config(state='normal')

def ok_command():
    status_window.withdraw()




