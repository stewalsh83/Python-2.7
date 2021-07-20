#!/usr/bin/env python

a = []
p = 0

s = raw_input()
while s != "end":
   n = int(s)
   a.append(n)
   s = raw_input()

i = input()
while i < len(a):
   if a[i] < a[p]:
      p = i
   i = i + 1
print p
