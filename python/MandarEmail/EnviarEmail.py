import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

# Criar o servidor e enviar e-mail

# 1 STARTAR O SERVIDOR SMTP
host = 'smtp.email.com'
port = '587'
login = 'email_envia@email.com'
ssh = 'taProcurandoOquePalhaço'

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(login, ssh)

# 2 CONSTRUIR O EMAIL TIPO MIME
corpo = '<b>Arquivo de mandar e-mail escrito em python!!!</b>'

# Montando e-mail
msg = MIMEMultipart()
msg['From'] = login
msg['To'] = 'email_recebe@email.com'
msg['Subject'] = 'Meu e-mail enviado por python'
msg.attach(MIMEText(corpo, 'html'))

# Abrimos o arquivo em modo leitura e binary
# Definir o caminho absoluto do caminho_de onde está o arquivo EnviarEmail
caminho_arquivo = './MandarEmail/EnviarEmail.py'
filename = 'EnviarEmail.py'
attachment = open(caminho_arquivo, 'rb')


# Lemos o arquivo no modo binario e jogamos codigicado em base 64 (que é o que o e-mail precisa)
att = MIMEBase('application', 'octet-stream')
att.set_payload((attachment).read())
encoders.encode_base64(att)

# ADCIONAMOS o cabeçalho no tipo anexo do email
att.add_header('Content-Disposition', "attachment; filename= %s" % filename)
# fechamos o arquivo
attachment.close()
# Colocamos o anexo no corpo do e-mail
msg.attach(att)

# 3 ENVIAR o ENAIL tipo MIME no SERVIDOR SMTP
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
