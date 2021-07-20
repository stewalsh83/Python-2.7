#!/usr/bin/env python

import sys

file = sys.argv[1]

with open(file, "w") as fd:
   message = sys.argv[2:]
   i = 0
   while i < len(message):
      fd.write(message[i] + "\n")
      i = i + 1
