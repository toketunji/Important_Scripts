#!/bin/python
# script written by Olu for ags_technology training
# all rights reserved
# 11/05/2017

import sys,datetime

def cal_interest (p,t,r):
        return p*t*r/100

def write_to_disk (data):
        text_file = open("data.txt", "w")
        time_stamp = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
        text_file.write("Timestamp: %s \t  %s" % (time_stamp, data))
        text_file.close()

if __name__ == '__main__':
        interest = cal_interest (float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))
        print "Interest is calculated as %0.2f percent " %interest
        info = 'P = ' + sys.argv[1] +  ' T = ' + sys.argv[1] + ' R = ' + sys.argv[3]
        write_to_disk (info)


