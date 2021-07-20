#!/usr/bin/env python

binary = ""
base = 16

digits = "0123456789abcdef"

n = input()
while n != 0:
   binary = digits[n % base] + binary
   n = n / base

print binary
