#!/usr/bin/env python

a = []
p = 0
s = raw_input()

while s != "end":
   s = int(s)
   a.append(s)
   s = raw_input()

i = 1
while i < len(a):
   v = a[i]
   p = i
   while 0 < p and v < a[p - 1]:
      a[p] = a[p - 1]
      p = p - 1
   a[p] = v

   i = i + 1

i = 0
while i < len(a):
   print a[i]
   i = i + 1
