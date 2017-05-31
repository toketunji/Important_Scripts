#!/bin/python

import sys

try:
	_name = float(sys.argv[1])
except:
	print 'This is an Error'
	sys.exit(1)
else:
	print 'Hello', _name, ', welcome to the workshop'


