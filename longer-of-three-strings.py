#!/usr/bin/env python

s = raw_input()
r = raw_input()
t = raw_input()

if len(s) > len(r) and len(s) > len(t):
   print s
elif len(r) > len(t) and len(r) > len(s):
   print r
else:
   print t
