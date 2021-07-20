#!/usr/bin/env python

s = raw_input()

s = s[len(s) - 1] + s[1: len(s) - 1] + s[0]
print s
