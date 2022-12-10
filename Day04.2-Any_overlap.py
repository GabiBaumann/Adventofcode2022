#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

    5-7,7-9 overlaps in a single section, 7.
    2-8,3-7 overlaps all of the sections 3 through 7.
    6-6,4-6 overlaps in a single section, 6.
    2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.
"""

"""
Get the max startpoint, look if it's less than or equal to min endpoint.
"""

count = 0

with open('Day04-Input', 'r') as file:
    for line in file:
        r1, r2 = line.split(',')
        rf1, rt1 = r1.split('-')
        rf2, rt2 = r2.split('-')

        rf1 = int(rf1)
        rt1 = int(rt1)
        rf2 = int(rf2)
        rt2 = int(rt2)

        max_start = max(rf1, rf2)
        min_end = min(rt1, rt2)

        if max_start <= min_end:
            count += 1

print(count)
