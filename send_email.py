import os
from email.message import EmailMessage
import ssl
import smtplib


def send_email(em_sender, em_password, em_receiver, subject, body, file_path):
    em = EmailMessage()
    em['From'] = em_sender
    em['To'] = em_receiver
    em['Subject'] = subject
    em.set_content(body)

    with open(file_path, "rb") as content_file:
        content = content_file.read()
        em.add_attachment(content, maintype='application', subtype='xlsx', filename='basic.xlsx')


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(em_sender, em_password)
        smtp.sendmail(em_sender, em_receiver, em.as_string())


