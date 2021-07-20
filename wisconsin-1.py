#!/usr/bin/env python

s = raw_input()
while s != "end":
   i = 0
   while i < len(s) and s[i] != ",":
      i = i + 1

   state = s[i + 1:i + 3]
   if state == "WI":
      print s[:i]
   s = raw_input()
