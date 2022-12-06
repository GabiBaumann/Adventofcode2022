#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

## Length of helper string with all unique characters required.
## That's signal length minus one, as one more is always worked on.
## So, use strlength = 3 for 6.1, strlength = 13 for 6.2
strlength = 3
#strlength = 13

clear_at = 0
pos = 0
lastchars = ""

with open('Day06-Input', 'r') as file:
    stream = file.read()

while pos < len(stream):
    next_one = stream[pos]
    lastchars += next_one
    str_count = len(lastchars)
    for i in range(strlength, -1, -1):
        if str_count - 2 < i:
            continue
        elif next_one == lastchars[i]:
            cl_pos = pos - strlength
            if cl_pos < 0:
                cl_pos = 0
            cl_pos += i
            clear_at = max(clear_at, cl_pos)
            break
    if clear_at < pos - strlength: # this is it
        print(pos+1, lastchars)
        break
    if str_count > strlength:
        lastchars = lastchars[1:]
    pos += 1
