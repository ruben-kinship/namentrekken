import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


fromaddr = "ruthdecoster@msn.com"
toaddr = "decosterruben@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "ik zend een mailtje via python"

body = "een geavanceerder mailtje via Python, met onderwerp enzo... en... wat vind je ervan?"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp-mail.outlook.com', 587)
server.starttls()
server.login(fromaddr, "sebastien1")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
