#!/usr/bin/env python

import sys
file = sys.argv[1]
with open(file, "r") as f:
   nums = f.read().split()

total = 0
i = 0
while i < len(nums):
   total = total + int(nums[i])
   i = i + 1
print total
