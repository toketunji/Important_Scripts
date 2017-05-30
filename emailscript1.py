#!/usr/bin/python

import smtplib

sender = 'toketunji"gmail.com'
receivers = 'jahdezzy"gmail.com'

message = """From: From Person <toketunji@gmail.com>
To: To Person <jahdezzy@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
smtpObj = smtplib.SMTP('smtp.googlemail.com', 587)
smtpObj.starttls()
smtpObj.sendmail(sender, receivers, message)         
print "Successfully sent email"
