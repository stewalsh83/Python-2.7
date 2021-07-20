#!/usr/bin/env python

import sys
file_name = sys.argv[1]

message = "Hello world.\n"

with open(file_name, "w") as fd:
   fd.write(message)
