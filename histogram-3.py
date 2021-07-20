#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s):
   n = int(s[i])
   n = n * "*"
   print n
   i = i + 1
