import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "shashwatsharma12304@gmail.com"
email_password = os.environ.get("email_password")
email_receiver = "shashwatsharma.dev@gmail.com"
subject = 'SMTP Server testing'
body = """
Its working!!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.SSLContext(ssl.PROTOCOL_TLS)  # Explicitly create SSL context
with smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
