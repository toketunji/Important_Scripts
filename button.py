#!/bin/python

import sys, cgi

print "Content-type:text/html\n\n"
print "<html>"
print "<head><title>My First CGI Script</title></head>"
print "<body>"
form = cgi.FieldStorage()
firstname = form.getvalue('firstname')
lastname = form.getvalue('lastname', '').upper()
sex = form.getvalue('gender')

print '<form method="post" action="button.py">'
print '<p>What is your First Name? <input type="text" name="firstname" /></p>'
print '<p>What is your Last Name? <input type="text" name="lastname" /></p>'

print '<p>What is your Gender? </p>'
print '<input type="radio" name="gender" value="Male">Male<br>'
print '<input type="radio" name="gender" value="Female">Female<br>'
print '<input type="submit" value="Submit" />'

if (len(firstname)) > 0 and (len(lastname)) > 0:
	print "<h1> Hello %s %s  Welcome to my Trinitas Ltd" % (firstname, lastname) + " and " + " Your Gender is %s</h1>" % (sex)
print "</form>"
print "</body>"
print "</html>"
