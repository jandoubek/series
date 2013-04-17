#!/usr/bin/perl -0

from dateutil import parser
import math

def trim_time(dates, values, from_date_str, to_date_str):
 from_date = parser.parse(from_date_str)
 to_date = parser.parse(to_date_str)

 trim_dates = []
 trim_values = []

 for i in range(len(dates)):
  if not (dates[i] > to_date or dates[i] < from_date):
   trim_dates.append(dates[i])
   trim_values.append(values[i]);
 return [trim_dates,trim_values]

import matplotlib.pyplot as plt

# Insert tuples of dates and values
def plot_series(series_tuples):

 #IMPLEMENT checking the sizez
 for serie in series_tuples:
  if not consistency_check(serie[0],serie[1]):
   return;
 
 #UNPACKING
 for serie in series_tuples:
  x_ser = serie[0]
  y_ser = serie[1]
  if len(serie) > 2:
   format_string = serie[2]
   plt.plot(x_ser,y_ser,format_string)
  else:
   plt.plot(x_ser,y_ser);
 
 plt.show()

def plot_serie(dates,values,style='b-'):
 if not consistency_check(dates,values):
  return
 
 dates_serie = []
 values_serie = []
 for i in range(len(dates)):
  dates_serie.append(parse_date(dates[i]))
  values_serie.append(float(values[i]))
 
 plt.plot(dates_serie,values_serie,style)
 plt.show()

def parse_date(date):
 return parser.parse(date) 

def consistency_check(l1,l2):
 if len(l1) <> len(l2):
  print "Inconsistent data, some data vs values has different sizes %s and %s " %(len(l1),len(l2))
  return False 
 return True

def moving_average(step, keys, values):
 
 #Test date sizes
 
 size = len(values)

 halfstep = step / 2
 averaged = []
 trimedkeys = []
 count = math.fsum(values[:step])
 for i in range(size-2*halfstep):
  averaged.append(count/step)
  trimedkeys.append(keys[i+halfstep])
  if i < size - halfstep - 1:
   count += values[i+halfstep+1]
   count -= values[i-halfstep];
 
 return [trimedkeys,averaged]
