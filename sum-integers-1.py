#!/usr/bin/env python

import sys
nums = sys.stdin.read().split()

total = 0
i = 0
while i < len(nums):
   total = total + int(nums[i])
   i = i + 1
print total
