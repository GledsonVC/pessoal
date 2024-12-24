import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

# quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

# ticket medio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})

# enviar um email com relatório

# 1 STARTAR O SERVIDOR SMTP
host = 'smtp.email.com'
port = '587'
login = 'emailenvia@email.com'
senha = 'taProcurandoOquePalhaço'

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(login, senha)

# 2 CONSTRUIR O EMAIL TIPO MIME
corpo = f''''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att</p>
<p>Gledson</p>
'''

# Montando e-mail
msg = MIMEMultipart()
msg['From'] = login
msg['To'] = 'emailrecebe@email.com'
msg['Subject'] = 'Relatório de Vendas por Loja'
msg.attach(MIMEText(corpo, 'html'))

# 3 ENVIAR o ENAIL tipo MIME no SERVIDOR SMTP
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print(f'Mensagem enviada com sucesso para {msg["To"]}')
