#!/usr/bin/env python

a = []
p = 0

line = raw_input()
while line != "end":
   n = int(line)
   a.append(line)
   line = raw_input()

i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1

   # swap a[i] and a[p] (check the order here carefully)
      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp
   i = i + 1

i = 0
while i < len(a):
   print a[i]# Fix me (write the output in the required format).
   i = i + 1
