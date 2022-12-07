#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

## Length of helper string with all unique characters required.
## That's signal length minus one, as one more is always worked on.
## Use strlength = 3 for 6.1, strlength = 13 for 6.2
#strlength = 3
strlength = 13

clear_at = 0
pos = 0

with open('Day06-Input', 'r') as file:
    stream = file.read()

for next_one in stream:
    for i in range(strlength):
        if pos - 1 < i:
            break
        elif next_one == stream[pos - i - 1]:
            clear_at = max(clear_at, pos - i)
            break
    pos += 1
    if clear_at < pos - strlength: # this is it
        print(pos, stream[pos-strlength-1:pos])
        break
