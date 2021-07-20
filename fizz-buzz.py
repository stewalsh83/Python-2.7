#!/usr/bin/env python

n = input()

i = 1
while i < n + 1:
   if i % 3 == 0 and i % 5 != 0:
      print "fizz"
   elif i % 5 == 0 and i % 3 != 0:
      print "buzz"
   elif i % 3 == 0 and i % 5 == 0:
      print "fizz-buzz"
   else:
      print i
   i = i + 1
