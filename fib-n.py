#!/usr/bin/env python

n = input()
prev = 0
curr = 1
print 0
i = 0
while i < n - 1:
   print curr
   old_curr = curr
   curr = prev + curr
   prev = old_curr
   i = i + 1
