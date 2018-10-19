"""The first step is to create an SMTP object, each object is used for connection
with one server."""

import smtplib
server = smtplib.SMTP('smtp-mail.outlook.com',587)
server.starttls() #protection needed to protect your password
#Next, log in to the server
server.login("ruthdecoster@msn.com", "*******")

#Send the mail
msg = """Testje van mezelf!\n
mailtje gestuurd vanuit Python.
Laat je weten als het toegekomen is?
Ik steek de code in onze github
Groetjes
Ruth
"""
# The /n separates the message from the headers, is dus nodig om tekst te hebben!
server.sendmail("ruthdecoster@msn.com", "decosterruben@gmail.com", msg)
server.quit()
