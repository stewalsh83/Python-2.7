#!/usr/bin/env python

total = 0
n = input()

while n != 0:
   if n > 0:
      total = total + n
   else:
      n = n * -1
      total = total + n
   n = input()

print total
