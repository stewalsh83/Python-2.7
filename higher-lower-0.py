#!/usr/bin/env python

n = input()
m = 0

while n != 0:
   m = input()
   if m < n:
      print "lower"
   elif n == m:
      print "equal"
   else:
      print "higher"
   n = m
