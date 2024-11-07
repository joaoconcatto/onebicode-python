from email.message import EmailMessage
import smtplib
import ssl

password = open('senha', 'r').read()

from_email = 'jgconcatto@gmail.com'
to_email = 'jgconcatto@gmail.com'
subject = 'Email automatizado entregue!'
body = '''
Automatização de processos é a melhor forma
de economizar seu tempo. Invista em Python!
'''


# 1- estruturando o email
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