#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, but the distress beacon must have x and y coordinates each no lower than 0 and no larger than 4000000.

To isolate the distress beacon's signal, you need to determine its tuning frequency, which can be found by multiplying its x coordinate by 4000000 and then adding its y coordinate.

In the example above, the search space is smaller: instead, the x and y coordinates can each be at most 20. With this reduced search area, there is only a single position that could have a beacon: x=14, y=11. The tuning frequency for this distress beacon is 56000011.

Find the only possible position for the distress beacon. What is its tuning frequency?
"""

"""
Now there's a grid to search.
So fill the grid with the sensor coverage, no need to care for beacons (they're all in range.

Well, this naive thing works fine for the example, 
but eats my memory while initializing the grid.

That should leave only one grid coordinate as blind spot.
Compute the coordinate's tuning frequency.
"""

max_grid = 4000000  # inclusive
#max_grid = 20       # for example input

sensorx = []
sensory = []
distance = []
range_starts = []
range_ends = []

with open('Day15-Input', 'r') as file:
    for line in file:
        d1,d2,sx,sy,d3,d4,d5,d6,bx,by = line.split()
        sx = int(sx[2:-1])
        sy = int(sy[2:-1])
        bx = int(bx[2:-1])
        by = int(by[2:])
        
        md = abs(sx-bx) + abs(sy-by)
        sensorx.append(sx)
        sensory.append(sy)
        distance.append(md)

for y in range(max_grid+1):
    range_starts = []
    range_ends = []
    for sensor in range(len(sensorx)):
        #print(sensor, sensorx[sensor], sensory[sensor], distance[sensor])
        dy = abs(y - sensory[sensor])
        if dy > distance[sensor]:
            #print("Line not in sensor coverage.", sensory[sensor], distance[sensor], dy)
            continue
        xr = distance[sensor] - dy
        xstart = sensorx[sensor] - xr
        xend = sensorx[sensor] + xr
        #print("Range on line", xstart, xend)
        if xstart < 0:
            xstart = 0
        if xend > max_grid:
            xend = max_grid
        if xstart == 0 and xend == max_grid: # this will come up again. move?
            #print("Full line at once")
            break
        handled_entry = False
        for i in range(len(range_starts)):
            handled_now = False
            if xstart < range_starts[i] and xend >= range_starts[i]:
                range_starts[i] = xstart
                handled_now = True
                handled_entry = True
            if xend > range_ends[i] and xstart <= range_ends[i]:
                range_ends[i] = xend
                handled_now = True
                handled_entry = True
            if xstart >= range_starts[i] and xend <= range_ends[i]:
                handled_now = True
                handled_entry = True
            if handled_now:
                xstart = range_starts[i]
                xend = range_ends[i]
        if handled_entry:
            #print("Folding ranges")
            # This still fucks up:
            # 3132904 [2713146, 2713146, 0] [3648476, 4000000, 2713144]
            didsth = True
            while didsth:
                didsth = False
                for i in range(len(range_starts) - 1):
                    if range_starts[i] >= range_starts[-1] and range_ends[i] <= range_ends[-1]:
                        range_starts.pop(i)
                        range_ends.pop(i)
                        didsth = True
                        break
                for i in range(1, len(range_starts)):
                    if range_starts[i] <= range_starts[0] and range_ends[i] >= range_ends[0]:
                        range_starts.pop(0)
                        range_ends.pop(0)
                        didsth = True
                        break
                    
        else:
            range_starts.append(xstart)
            range_ends.append(xend)
    #if not range_starts:
    #    print("Did not do range, just dropped here")
    #    continue
    if range_starts[0] > 0 or range_ends[0] < max_grid:
        print("This should be the result line.")
        print(y, range_starts, range_ends)
        break   # This is it.

for i in range_ends:
    if i < max_grid:
        break
out = y + (i + 1) * 4000000 #max_grid
print(out)

# 10852583132904
