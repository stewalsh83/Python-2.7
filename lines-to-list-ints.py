#!/usr/bin/env python

a = []
s = raw_input()

while s != "end":
   # a = a + [n]
   a.append(int(s))
   s = raw_input()

print a
