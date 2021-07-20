#!/usr/bin/env python

import sys

translation = {}

with open("translation.txt", "r") as fd:
   lines = fd.readlines()

i = 0
while i < len(lines):
   words = lines[i].split()
   translation[words[0]] = words[1]
   i += 1

nums = sys.stdin.readlines()
i = 0
while i < len(nums):
   eng = nums[i].strip()
   if eng in translation:
      print translation[eng]
   i += 1
