#!/usr/bin/env python

n = input()

if n % 3 == 0 and n % 5 != 0:
   print "fizz"
elif n % 5 == 0 and n % 3 != 0:
   print "buzz"
elif n % 3 == 0 and n % 5 == 0:
   print "fizz-buzz"
else:
   print n
