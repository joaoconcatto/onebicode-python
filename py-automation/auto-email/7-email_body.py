from email.message import EmailMessage
import ssl
import smtplib

password = open('senha', 'r').read()
from_email = 'jgconcatto@gmail.com'
to_email = 'jgconcatto@gmail.com'
subject = 'Atividade aceita!'
body = open('auto-email/files/body.txt', 'r', encoding='utf-8').read()


# 1- montando a estrutura do e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()


# 2- envio de email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )


