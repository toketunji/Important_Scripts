#!/bin/python
# script modified by Tope for ags_technology training
# all rights reserved
# 11/05/2017

import sys, MySQLdb

db = MySQLdb.connect(host="localhost",user="root",passwd="root",db="Billing")


cursor = db.cursor()

def cal_interest (p,t,r):
        return p*t*r/100

#cursor.execute(sql_command)
# Commit your changes in the database

def write_to_db (p,t,r,I):

	cursor.execute("INSERT INTO Interest (Principal, Time, Rate, Interest) VALUES ('"+ str(p) +"', '"+ str(t) +"', '"+ str(r) +"', '"+ str(I)+ "');")

	db.commit()

if __name__ == '__main__':
        I = cal_interest (float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))
        print "Interest is calculated as %0.2f percent " % I
	#info = ' p = ' + sys.argv[1] + ' t = ' + sys.argv[2] + ' r = ' + sys.argv[3] + ' I = ' + I
	write_to_db (sys.argv[1], sys.argv[2], sys.argv[3], I)
# disconnect from server
db.close()
