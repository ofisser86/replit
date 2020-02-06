import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

import u2020system

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Didi'
email['to'] = 'reworkmind@gmail.com'
email['subject'] = 'You won 1000000000 dollars'

context = {
    'name': 'Di',
    'name2': 'di'
}

email.set_content(html.substitute(context), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('zalka.x96h@gmail.com', u2020system.email_password)
    smtp.send_message(email)
    print('all good message sent')
