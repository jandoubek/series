#!/usr/bin/python

import unittest
import series

class UnitTestSeries(unittest.TestCase):
 
 def test_date_parsing(self):
  datestr = '2013/03/27 07:34:26'
  etalon = series.parse_date(datestr)

  datestr = '2013.03.27 07:34:26'
  self.assertTrue(etalon == series.parse_date(datestr))

  datestr = '27.03.2013 07:34:26'  
  self.assertTrue(etalon == series.parse_date(datestr))

  datestr = '27.March.2013 07:34:26'  
  self.assertTrue(etalon == series.parse_date(datestr))

  datestr = '27.Brezen.2013 07:34:26'  
  self.assertTrue(etalon == series.parse_date(datestr))



if __name__ == '__main__':
 unittest.main()
  
