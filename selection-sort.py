#!/usr/bin/env python

a = []
p = 0

s = raw_input()
while s != "end":
   n = int(s)
   a.append(n)
   s = raw_input()

i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   temp = a[p]
   a[p] = a[i]
   a[i] = temp
   i = i + 1

i = 0
while i < len(a):
   print a[i]
   i = i + 1
