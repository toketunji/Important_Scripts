#!/bin/python

import os,shutil,time
from datetime import datetime,timedelta

now = time.time()
three_days_ago = now - (3 * 86400)

path='/home/ec2-user/logging/'

for file in os.listdir(path):
        t = os.stat(str(path) + file)
        filetime = t.st_mtime
        #filetime = time.ctime(os.path.getmtime(os.path.join(path, file)))

        if filetime < three_days_ago:
                print "File  [ %s ] is older than 3 days  " % file
                print  'copying %s' % file
		shutil.copy ('/home/ec2-user/logging/' + file,'/tmp/dump/b_/')
