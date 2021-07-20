#!/usr/bin/env python

import sys
cypher = {}

low = "abcdefghijklmnopqrstuvwxyz"
cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowcap = low + cap
other = low[13:] + low[:13] + cap[13:] + cap[:13]

i = 0
while i < len(lowcap):
   cypher[lowcap[i]] = other[i]
   i += 1

text = sys.stdin.readlines()
i = 0
while i < len(text):
   line = text[i].strip()
   j = 0
   total = ""
   while j < len(line):
      if line[j] in cypher:
         total += cypher[line[j]]
      else:
         total = total + line[j]
      j += 1
   print(total)
   i += 1
