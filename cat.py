#!/usr/bin/env python

import sys

file = sys.argv[1]
message = sys.stdin.readlines(1:)

with open(file, "r") as fd:
   message = sys.argv[2:]
   i = 0
   while i < len(message):
      fd.readlines(message[i])
      i = i + 1
