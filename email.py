import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Pratish Bajpai'
email['to'] = 'pratishbajpai7@gmail.com'
email['subject'] = 'test'

email.set_content('ningal')

with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pratishbajpai6@gmail.com', 'Pratish7@123')
    smtp.send_message(email)
    print('sent')
