#!/usr/bin/env python

even = []
odd = []

s = raw_input()
while s != "end":
   if int(s) % 2 == 0:
      even.append(s)
   else:
      odd.append(s)
   s = raw_input()

i = 0
while i < len(even):
   print even[i]
   i = i + 1

i = 0
while i < len(odd):
   print odd[i]
   i = i + 1
