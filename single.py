#!/usr/bin/python -O

import sys

filename = sys.argv[1]
print "Opening the %s" %(filename)
f = open(filename,'r')
filelines = f.readlines()

dates_str = []
values_str = []
print "Slicing the data"
for line in filelines:
    tokens = line.split(',')
    dates_str.append(tokens[0])
    values_str.append(tokens[1])

import series
print "Plotting the data"
series.plot_serie(dates_str,values_str)
