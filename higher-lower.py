#!/usr/bin/env python

n = input()
m = 0

i = 0
while i < 5:
   m = input()
   if m < n:
      print "lower"
   elif n == m:
      print "equal"
   else:
      print "higher"
   n = m
   i = i + 1
