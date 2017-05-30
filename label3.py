#!/bin/python
# script written by Olu for ags_technology training
# all rights reserved
# 11/05/2017

import sys

def cal_interest (p,t,r):
        return p*t*r/100

if __name__ == '__main__':
        interest = cal_interest (float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))
        print "Interest is calculated as %0.2f percent " % interest

