from email.message import EmailMessage
import ssl
import smtplib
import mimetypes


password = open('senha', 'r').read()
from_email = 'jgconcatto@gmail.com'
to_email = 'jgconcatto@gmail.com'
subject = 'Notícia diária sobre investimentos'
body = open('auto-email/files/body_bb.txt', 'r', encoding='utf-8').read()


# 1- montando a estrutura do e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()


# 2- adicionar anexos (arquivos baixáveis)
anexo = 'auto-email/bb_preco.png'

mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')

with open(anexo, 'rb') as a:
    message.add_attachment(
        a.read(),
        maintype = mime_type,
        subtype = mime_subtype,
        filename = 'Gráfico Preço x Tempo'
    )


# 3- envio de email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )