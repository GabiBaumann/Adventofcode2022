#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, and that doesn't make any sense. However, you do notice a little path that leads behind the waterfall.

Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and the signal definitely leads further inside.

As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!

Fortunately, your familiarity with analyzing the path of falling material will come in handy here. You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly air with structures made of rock.

Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, where x represents distance to the right and y represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:

498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9

This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. (Specifically, the first path consists of a line of rock from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.)

The sand is pouring into the cave from point 500,0.

Drawing rock as #, air as ., and the source of the sand as +, this becomes:


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.

Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. A unit of sand is large enough to fill one tile of air in your scan.

A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.

So, drawing sand that has come to rest as o, the first unit of sand simply falls straight down and then stops:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......o.#.
#########.

The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
.....oo.#.
#########.

After a total of five units of sand have come to rest, they form this pattern:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
....oooo#.
#########.

After a total of 22 units of sand:

......+...
..........
......o...
.....ooo..
....#ooo##
....#ooo#.
..###ooo#.
....oooo#.
...ooooo#.
#########.

Finally, only two more units of sand can possibly come to rest:

......+...
..........
......o...
.....ooo..
....#ooo##
...o#ooo#.
..###ooo#.
....oooo#.
.o.ooooo#.
#########.

Once all 24 units of sand shown above have come to rest, all further sand flows out the bottom, falling into the endless void. Just for fun, the path any new sand takes before falling forever is shown here with ~:

.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........

Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?
"""

"""
First "paint" the paths into a grid:
    if new x  > width(grid): Expand grid by x - len(grid) in each row.
    if new y > height(grid): Expand grid by y - height(grid) new rows.
    (Or else go through all input or full row to find max(x) and max(y))
    Init all fields to 0.
    Paint the paths: All coordinates covered by stone are set to 1.
Sand flows from 500,0:
    if x, y+1 is 0, this is next pos.
    if x-1, y+1 is 0, this is next pos
    if x+1, y+1 is 0, this is next pos
    if y + 1 = height(grid): Sand flows through.
    else (comes to rest): set x,y to 2. Increase sand counter.
    (Actually, path and sand can both be True, init to False.)
"""

def draw_path(x,y,px,py):
    if x == px:
        if y < py:
            for i in range(y,py+1):
                grid[i][x] = True
        else:
            for i in range(py,y+1):
                grid[i][x] = True
    else:
        if x < px:
            for i in range(x,px+1):
                grid[y][i] = True
        else:
            for i in range(px,x+1):
                grid[y][i] = True

grid = []
sandx = 500
sandy = 0

for y in range(200):
    grid.append([])
    for x in range(700):
        grid[y].append(False)

with open('Day14-Input') as file:
    for line in file:
        start = True
        x, y = 0, 0
        while "-" in line:
            coordinates, line = line.split(' ', 1)
            if coordinates == "->":
                continue
            px = x
            py = y
            x, y = coordinates.split(',')
            if start:
                start = False
                continue
            draw_path(int(x),int(y),int(px),int(py))
        px = x
        py = y
        x,y = line.split(',')
        draw_path(int(x),int(y),int(px),int(py))

flow_off = len(grid) - 1
filled = False
count = 0

while not filled:
    count += 1
    x = sandx
    y = sandy
    while True:
        y += 1
        if y == flow_off:
            filled = True
            break
        elif not grid[y][x]:
            continue
        elif not grid[y][x-1]:
            x -= 1
            continue
        elif not grid[y][x+1]:
            x += 1
            continue
        grid[y-1][x] = True
        break

print(count-1)

# 885

"""
for y in range(20):
    st = ''
    for x in range(480,520):
        if grid[y][x]:
            st += "#"
        else:
            st += "."
    print(st)
"""
