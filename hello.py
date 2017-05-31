#!/bin/python

import sys, cgi

print "Content-type:text/html\n\n"
print "<html>"
print "<head><title>My First CGI Script</title></head>"
print "<body>"
form = cgi.FieldStorage()
firstname = form.getvalue('firstname')
lastname = form.getvalue('lastname', '').upper()
print '<form method="post" action="hello.py">'
print '<p>What is your First Name? <input type="text" name="firstname" /></p>'
print '<p>What is your Last Name? <input type="text" name="lastname" /></p>'
print "<h1> Hello %s %s  Welcome to my Python Class!</h1><br />" % (firstname, lastname)
print '<input type="submit" value="Submit" />'
print "</form>"
print "</body>"
print "</html>"
