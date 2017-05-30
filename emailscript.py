import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print 'Script demonstrates How To send emails using Python'
print '==================================================='
print ''

yLogin = "temitope.oketunji@talktalk.net"
yPassword = "Salvation3."

server = smtplib.SMTP('smtp.talktalk.net', 587) #smtp,port number
server.ehlo()
server.starttls()
server.ehlo()

server.login (yLogin, yPassword)

fromaddr = "temitope.oketunji@talktalk.net"
toaddr = "temitope.oketunji@talktalk.net"
subject = "From Python"


msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject

body = "Sent from Python"

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

print 'message sent'
