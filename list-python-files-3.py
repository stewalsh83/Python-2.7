#!/usr/bin/env python

import os
files = os.listdir(".")
shebang = "#!/usr/bin/env python\n"

i = 0
while i < len(files):
    file = files[i]
    with open(file, "r") as fd:
        line = fd.readline()
        if len(line) != 0:
            if file[-3:] == ".py" or line == shebang:
                print file
    i = i + 1
