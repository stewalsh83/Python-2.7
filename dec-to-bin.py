#!/usr/bin/env python

binary = ""
base = 2

digits = "01"

n = input()
while n != 0:
   binary = digits[n % base] + binary
   n = n / base

print binary
