#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
You enter a large crater of gray dirt where the grove is supposed to be. All around you, plants you imagine were expected to be full of fruit are instead withered and broken. A large group of Elves has formed in the middle of the grove.

"...but this volcano has been dormant for months. Without ash, the fruit can't grow!"

You look up to see a massive, snow-capped mountain towering above you.

"It's not like there are other active volcanoes here; we've looked everywhere."

"But our scanners show active magma flows; clearly it's going somewhere."

They finally notice you at the edge of the grove, your pack almost overflowing from the random star fruit you've been collecting. Behind you, elephants and monkeys explore the grove, looking concerned. Then, the Elves recognize the ash cloud slowly spreading above your recent detour.

"Why do you--" "How is--" "Did you just--"

Before any of them can form a complete question, another Elf speaks up: "Okay, new plan. We have almost enough fruit already, and ash from the plume should spread here eventually. If we quickly plant new seedlings now, we can still make it to the extraction point. Spread out!"

The Elves each reach into their pack and pull out a tiny plant. The plants rely on important nutrients from the ash, so they can't be planted too close together.

There isn't enough time to let the Elves figure out where to plant the seedlings themselves; you quickly scan the grove (your puzzle input) and note their positions.

For example:

....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..

The scan shows Elves # and empty ground .; outside your scan, more empty ground extends a long way in every direction. The scan is oriented so that north is up; orthogonal directions are written N (north), S (south), W (west), and E (east), while diagonal directions are written NE, NW, SE, SW.

The Elves follow a time-consuming process to figure out where they should each go; you can speed up this process considerably. The process consists of some number of rounds during which Elves alternate between considering where to move and actually moving.

During the first half of each round, each Elf considers the eight positions adjacent to themself. If no other Elves are in one of those eight positions, the Elf does not do anything during this round. Otherwise, the Elf looks in each of four directions in the following order and proposes moving one step in the first valid direction:

    If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
    If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
    If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
    If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.

After each Elf has had a chance to propose a move, the second half of the round can begin. Simultaneously, each Elf moves to their proposed destination tile if they were the only Elf to propose moving to that position. If two or more Elves propose moving to the same position, none of those Elves move.

Finally, at the end of the round, the first direction the Elves considered is moved to the end of the list of directions. For example, during the second round, the Elves would try proposing a move to the south first, then west, then east, then north. On the third round, the Elves would first consider west, then east, then north, then south.

As a smaller example, consider just these five Elves:

.....
..##.
..#..
.....
..##.
.....

The northernmost two Elves and southernmost two Elves all propose moving north, while the middle Elf cannot move north and proposes moving south. The middle Elf proposes the same destination as the southwest Elf, so neither of them move, but the other three do:

..##.
.....
..#..
...#.
..#..
.....

Next, the northernmost two Elves and the southernmost Elf all propose moving south. Of the remaining middle two Elves, the west one cannot move south and proposes moving west, while the east one cannot move south or west and proposes moving east. All five Elves succeed in moving to their proposed positions:

.....
..##.
.#...
....#
.....
..#..

Finally, the southernmost two Elves choose not to move at all. Of the remaining three Elves, the west one proposes moving west, the east one proposes moving east, and the middle one proposes moving north; all three succeed in moving:

..#..
....#
#....
....#
.....
..#..

At this point, no Elves need to move, and so the process ends.

The larger example above proceeds as follows:

== Initial State ==
..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............

== End of Round 1 ==
..............
.......#......
.....#...#....
...#..#.#.....
.......#..#...
....#.#.##....
..#..#.#......
..#.#.#.##....
..............
....#..#......
..............
..............

== End of Round 2 ==
..............
.......#......
....#.....#...
...#..#.#.....
.......#...#..
...#..#.#.....
.#...#.#.#....
..............
..#.#.#.##....
....#..#......
..............
..............

== End of Round 3 ==
..............
.......#......
.....#....#...
..#..#...#....
.......#...#..
...#..#.#.....
.#..#.....#...
.......##.....
..##.#....#...
...#..........
.......#......
..............

== End of Round 4 ==
..............
.......#......
......#....#..
..#...##......
...#.....#.#..
.........#....
.#...###..#...
..#......#....
....##....#...
....#.........
.......#......
..............

== End of Round 5 ==
.......#......
..............
..#..#.....#..
.........#....
......##...#..
.#.#.####.....
...........#..
....##..#.....
..#...........
..........#...
....#..#......
..............

After a few more rounds...

== End of Round 10 ==
.......#......
...........#..
..#.#..#......
......#.......
...#.....#..#.
.#......##....
.....##.......
..#........#..
....#.#..#....
..............
....#..#..#...
..............

To make sure they're on the right track, the Elves like to check after round 10 that they're making good progress toward covering enough ground. To do this, count the number of empty ground tiles contained by the smallest rectangle that contains every Elf. (The edges of the rectangle should be aligned to the N/S/E/W directions; the Elves do not have the patience to calculate arbitrary rectangles.) In the above example, that rectangle is:

......#.....
..........#.
.#.#..#.....
.....#......
..#.....#..#
#......##...
....##......
.#........#.
...#.#..#...
............
...#..#..#..

In this region, the number of empty ground tiles is 110.

Simulate the Elves' process and find the smallest rectangle that contains the Elves after 10 rounds. How many empty ground tiles does that rectangle contain?
"""

"""
Record the elves into a x/y 2dim list. Perhaps offset by 10 to allow any movement. 

Conflict can only happen if there's an elf two squares in the direction of travel chosen. Keep tabs of conflicts, if second elf in a conflict moves towards first elf, undo first elf move, don't do second elves move.

Nope. While each elf can only cause one conflict, it may be target to two of them. Multiple resets are no good. Wait: reset it to its pos recorded in cs (conflict source) will do.

Nope again. Tests of elfs further down the line go wrong if elf did move.
Really need to have a copy of the grid, do (and undo) all moves there,
replace original with copy when done.

Instead of switching choice of directions, the map could be transformed. (180 degrees, 90 degrees clockwise, 180 degrees, 90 degrees clockwise...)

After 10 steps, rectangle is defined by minx, miny, maxx, maxy of elves positions. Sub total number of elves.

Todo: make grids consist of False/True rather than ''/'#'

Uaah: If no other elves are on any of the 8 surrounding pos, it does nothing!
"""

from copy import deepcopy as cp

def move_elf(x, y):
    avoid = []
    resetelf = []
    for i in range(len(ct)):
        print(i, len(ct), "conflict list debug")
        if (x, y) == ct[i]:
            print(x,y, cdir[i], 'in conflict list')
            avoid.append(cdir[i])
            resetelf.append(cs[i])
            # optional, should be faster.
            #cs.pop(i)
            #ct.pop(i)
            #cdir.pop(i)
    for check_dir in rc:
        if check_dir == 'u':
            if 'u' in avoid:
                # this move conflics. don't move,
                # reset origin elf, which has moved down.
                for i in range(len(avoid)):
                    if avoid[i] == 'u':
                        a, b = resetelf[i][0], resetelf[i][1]
                        nextgrid[b+1][a] = ''
                        nextgrid[b][a] = '#'
                break
            elif grid[y-1][x-1] == '#' or grid[y-1][x] == '#' or grid[y-1][x+1] == '#':
                continue
            # the move
            print("moving up", x, y)
            nextgrid[y-1][x] = '#'
            nextgrid[y][x] = ''
            break
        elif check_dir == 'd':
            print("Debug, d", x, y)
            if grid[y+1][x-1] or grid[y+1][x] or grid[y+1][x+1]:
                continue
            elif grid[y+2][x]: 
                cs.append((x,y))
                ct.append((x,y+2))
                cdir.append('u')
            # move
            print("moving down", x,y)
            nextgrid[y+1][x] = '#'
            nextgrid[y][x] = ''
            break
        elif check_dir == 'l':
            if 'l' in avoid:
                for i in range(len(avoid)):
                    if avoid[i] == 'l':
                        a, b = resetelf[i][0], resetelf[i][1]
                        nextgrid[b][a+1] = ''
                        nextgrid[b][a] = '#'
                break
            elif grid[y-1][x-1] or grid[y][x-1] or grid[y+1][x-1]:
                continue
            # move
            print('moving left', x,y)
            nextgrid[y][x-1] = '#'
            nextgrid[y][x] = ''
            break
        elif check_dir == 'r':
            if grid[y-1][x+1] or grid[y][x+1] or grid[y+1][x+1]:
                continue
            elif grid[y][x+2]:
                cs.append((x,y))
                ct.append((x+2,y))
                cdir.append('l')
            # move
            print('moving right', x,y)
            nextgrid[y][x+1] = '#'
            nextgrid[y][x] = ''
            break


offset = 10
no_elfs = 0

rule = [ 'u', 'd', 'l', 'r' ]
grid = []
for i in range(offset):
    grid.append([])

with open('Day23-Input--Debug', 'r') as file:
#with open('Day23-Input', 'r') as file:
    y = 0
    for line in file:
        l = []
        for i in range(offset):
            l.append('')
        for char in line.rstrip():
            if char == '#':
                l.append(char)
                no_elfs += 1
            else:
                l.append('')
        for i in range(offset):
            l.append('')
        grid.append(l)
        y += 1

for i in range(offset):
    grid.append([])
    for j in range(len(grid[offset+1])):
        grid[i].append('')
        grid[-1].append('')

print(no_elfs, "elfs on the grid.")
#print(grid)
for i in range(len(grid)):
    print(len(grid[i]), grid[i])
for i in range(len(grid)):
    o=''
    for j in range(len(grid[0])):
        o = o + grid[i][j].replace('', '.').replace('.#.', '#')
    print(o)

for count in range(10):
    rc = [rule[count%4],rule[(count+1)%4],rule[(count+2)%4],rule[(count+3)%4]]
    print('Ruleset:', rc)
    nextgrid = cp(grid)
    cs = []
    ct = []
    cdir = [] # all these should be auto-empty, but this anchors to global.
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] and (grid[y-1][x-1] or grid[y-1][x] or grid[y-1][x+1] or grid[y][x-1] or grid[y][x+1] or grid[y+1][x-1] or grid[y+1][x] or grid[y+1][x+1]):
                move_elf(x, y) # rc and conflict lists are global
    grid = cp(nextgrid)
    for i in range(len(grid)):
        o=''
        for j in range(len(grid[0])):
            o += grid[i][j].replace('', '.').replace('.#.', '#')
        print(o)
# Main loop done.

# get min/max x/y
miny = len(grid)
maxy = 0
minx = len(grid[0])
maxx = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x]:
            miny = min(miny, y)
            maxy = max(maxy, y)
            minx = min(minx, x)
            maxx = max(maxx, x)

print(minx, miny, maxx, maxy, no_elfs)
print((1+maxy-miny) * (1+maxx-minx) - no_elfs)

## mööp.
# 4165 is too high

# example is right:
# 110
# but elf distribution goes wrong in round 2
