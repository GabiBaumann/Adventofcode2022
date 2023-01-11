#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
With everything replanted for next year (and with elephants and monkeys to tend the grove), you and the Elves leave for the extraction point.

Partway up the mountain that shields the grove is a flat, open area that serves as the extraction point. It's a bit of a climb, but nothing the expedition can't handle.

At least, that would normally be true; now that the mountain is covered in snow, things have become more difficult than the Elves are used to.

As the expedition reaches a valley that must be traversed to reach the extraction site, you find that strong, turbulent winds are pushing small blizzards of snow and sharp ice around the valley. It's a good thing everyone packed warm clothes! To make it across safely, you'll need to find a way to avoid them.

Fortunately, it's easy to see all of this from the entrance to the valley, so you make a map of the valley and the blizzards (your puzzle input). For example:

#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#

The walls of the valley are drawn as #; everything else is ground. Clear ground - where there is currently no blizzard - is drawn as .. Otherwise, blizzards are drawn with an arrow indicating their direction of motion: up (^), down (v), left (<), or right (>).

The above map includes two blizzards, one moving right (>) and one moving down (v). In one minute, each blizzard moves one position in the direction it is pointing:

#.#####
#.....#
#.>...#
#.....#
#.....#
#...v.#
#####.#

Due to conservation of blizzard energy, as a blizzard reaches the wall of the valley, a new blizzard forms on the opposite side of the valley moving in the same direction. After another minute, the bottom downward-moving blizzard has been replaced with a new downward-moving blizzard at the top of the valley instead:

#.#####
#...v.#
#..>..#
#.....#
#.....#
#.....#
#####.#

Because blizzards are made of tiny snowflakes, they pass right through each other. After another minute, both blizzards temporarily occupy the same position, marked 2:

#.#####
#.....#
#...2.#
#.....#
#.....#
#.....#
#####.#

After another minute, the situation resolves itself, giving each blizzard back its personal space:

#.#####
#.....#
#....>#
#...v.#
#.....#
#.....#
#####.#

Finally, after yet another minute, the rightward-facing blizzard on the right is replaced with a new one on the left facing the same direction:

#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#

This process repeats at least as long as you are observing it, but probably forever.

Here is a more complex example:

#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#

Your expedition begins in the only non-wall position in the top row and needs to reach the only non-wall position in the bottom row. On each minute, you can move up, down, left, or right, or you can wait in place. You and the blizzards act simultaneously, and you cannot share a position with a blizzard.

In the above example, the fastest way to reach your goal requires 18 steps. Drawing the position of the expedition as E, one way to achieve this is:

Initial state:
#E######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#

Minute 1, move down:
#.######
#E>3.<.#
#<..<<.#
#>2.22.#
#>v..^<#
######.#

Minute 2, move down:
#.######
#.2>2..#
#E^22^<#
#.>2.^>#
#.>..<.#
######.#

Minute 3, wait:
#.######
#<^<22.#
#E2<.2.#
#><2>..#
#..><..#
######.#

Minute 4, move up:
#.######
#E<..22#
#<<.<..#
#<2.>>.#
#.^22^.#
######.#

Minute 5, move right:
#.######
#2Ev.<>#
#<.<..<#
#.^>^22#
#.2..2.#
######.#

Minute 6, move right:
#.######
#>2E<.<#
#.2v^2<#
#>..>2>#
#<....>#
######.#

Minute 7, move down:
#.######
#.22^2.#
#<vE<2.#
#>>v<>.#
#>....<#
######.#

Minute 8, move left:
#.######
#.<>2^.#
#.E<<.<#
#.22..>#
#.2v^2.#
######.#

Minute 9, move up:
#.######
#<E2>>.#
#.<<.<.#
#>2>2^.#
#.v><^.#
######.#

Minute 10, move right:
#.######
#.2E.>2#
#<2v2^.#
#<>.>2.#
#..<>..#
######.#

Minute 11, wait:
#.######
#2^E^2>#
#<v<.^<#
#..2.>2#
#.<..>.#
######.#

Minute 12, move down:
#.######
#>>.<^<#
#.<E.<<#
#>v.><>#
#<^v^^>#
######.#

Minute 13, move down:
#.######
#.>3.<.#
#<..<<.#
#>2E22.#
#>v..^<#
######.#

Minute 14, move right:
#.######
#.2>2..#
#.^22^<#
#.>2E^>#
#.>..<.#
######.#

Minute 15, move right:
#.######
#<^<22.#
#.2<.2.#
#><2>E.#
#..><..#
######.#

Minute 16, move right:
#.######
#.<..22#
#<<.<..#
#<2.>>E#
#.^22^.#
######.#

Minute 17, move down:
#.######
#2.v.<>#
#<.<..<#
#.^>^22#
#.2..2E#
######.#

Minute 18, move down:
#.######
#>2.<.<#
#.2v^2<#
#>..>2>#
#<....>#
######E#

What is the fewest number of minutes required to avoid the blizzards and reach the goal?
"""

"""
This thing is 35x100, it repeats itself after 700 steps.
(Example is 4x6, repeating after 12 steps).

First hunch: iterate a whole period, saving all empty floor tiles for each step.
Recurse through possible moves, preferring towards exit.

So iterate through grids until grid[n] = grid[0].
Optimum without blizzards is 99+34+2 steps taken.
Waiting adds one minute, moving left or up two.
"""

"""
As the expedition reaches the far side of the valley, one of the Elves looks especially dismayed:

He forgot his snacks at the entrance to the valley!

Since you're so good at dodging blizzards, the Elves humbly request that you go back for his snacks. From the same initial conditions, how quickly can you make it from the start to the goal, then back to the start, then back to the goal?

In the above example, the first trip to the goal takes 18 minutes, the trip back to the start takes 23 minutes, and the trip back to the goal again takes 13 minutes, for a total time of 54 minutes.

What is the fewest number of minutes required to reach the goal, go back to the start, then reach the goal again?
"""

"""
Do the visited list in triplicate and adress by run ID,
or cp from the initial round afresh.

Keep counting steps without break,
but add one for last step each trip.

Compute a list of startpoints from the back,
and either provide the goal as variable, 
or do a copy of the recursion function -- that should help a bit by sane first paths.
Maybe not too important, though.

Also: The starting points need to just use every consecutive point: it may be the right starttime.
"""

from copy import deepcopy as cp
from sys import setrecursionlimit
setrecursionlimit(10000)

template_visited = []
path = []
l_paths = []
blz = {}
line_no = 0
index = 0
not_repeated = True
starttimes = []
starttimes_end = []
cutoff = 10000
direction = 1

def find_path(step, y, x):
    global cutoff

    if y == targety and x == targetx:
        #print(step, 'me there!')
        return step
    if step in visited[y][x]:
        return cutoff
    visited[y][x].append(step)
    step += 1
    pit = step % full_circle
    if step >= cutoff - ((targety - y) + (targetx - x)) * direction:
        return cutoff
    if targety - (y * direction + direction) >= 0 and l_paths[pit][y+direction][x]:
        result = find_path(step, y+direction, x)
        cutoff = min(cutoff, result)
    if targetx - (x * direction + direction) >= 0 and l_paths[pit][y][x+direction]:
        result = find_path(step, y, x+direction)
        cutoff = min(cutoff, result)
    if l_paths[pit][y][x]: #wait
        result = find_path(step, y, x)
        cutoff = min(cutoff, result)
    if starty + y * direction + direction >= 0 and l_paths[pit][y-direction][x]:
        result = find_path(step, y-direction, x)
        cutoff = min(cutoff, result)
    if startx + x * direction + direction >= 0 and l_paths[pit][y][x-direction]:
        result = find_path(step, y, x-direction)
        cutoff = min(cutoff, result)
    return cutoff

#with open('Day24-Input--Debug', 'r') as file:
with open('Day24-Input', 'r') as file:
    for line in file:
        line = line.rstrip().strip('#')
        if line == '.':
            continue
        v_init = []
        p_init = []
        for i in range(len(line)):
            v_init.append([])
            if line[i] == '.':
                p_init.append(True)
                continue
            p_init.append(False)
            blz[index] = {}
            blz[index]['x'] = i
            blz[index]['y'] = line_no
            blz[index]['d'] = line[i]
            index += 1
        template_visited.append(v_init)
        path.append(p_init)
        line_no += 1
        
maxcol = len(path[0])
maxline = line_no
startx = 0
starty = 0
targetx = maxcol - 1
targety = maxline - 1
print('maxcol', maxcol, 'maxline', maxline)
l_paths.append(cp(path))

while True:
    for y in range(maxline):
        for x in range(maxcol):
            path[y][x] = True
    for index in blz:
        if blz[index]['d'] == '<':
            blz[index]['x'] = (blz[index]['x'] - 1) % maxcol
        elif blz[index]['d'] == '>':
            blz[index]['x'] = (blz[index]['x'] + 1) % maxcol
        elif blz[index]['d'] == '^':
            blz[index]['y'] = (blz[index]['y'] - 1) % maxline
        else:
            blz[index]['y'] = (blz[index]['y'] + 1) % maxline
        path[blz[index]['y']][blz[index]['x']] = False
    if path == l_paths[0]:
        break
    l_paths.append(cp(path))
full_circle = len(l_paths)
print(full_circle)

for i in range(full_circle):
    if l_paths[i][0][0]:
        starttimes.append(i)
    if l_paths[i][-1][-1]:
        starttimes_end.append(i)
print('Starttimes front:', starttimes)
print('Starttimes end:', starttimes_end)

for st in starttimes:
    visited = cp(template_visited)
    result = find_path(st, starty, startx)
    cutoff = min(cutoff, result)
print('First pass:', cutoff+1)

while starttimes_end[0] <= cutoff + 2:
    starttimes_end.append(starttimes_end.pop(0) + full_circle)
cutoff = 10000
direction = -1
startx = targetx
starty = targety
targetx = 0
targety = 0
for st in starttimes_end:
    print('Go back at', st)
    visited = cp(template_visited)
    result = find_path(st, starty, startx)
    cutoff = min(cutoff, result)
print('Way back:', cutoff+1)

while starttimes[0] <= cutoff + 2:
    starttimes.append(starttimes.pop(0) + full_circle)
cutoff = 10000
direction = 1
targetx = startx
targety = starty
startx = 0
starty = 0
for st in starttimes:
    print('Go again at', st)
    visited = cp(template_visited)
    result = find_path(st, starty, startx)
    cutoff = min(cutoff, result)
print('Finally:', cutoff+1)

# Result pt2:
"""
First pass: 247
Way back: 465
Finally: 695

695 is too low.
"""

# Example pt2:
"""
First pass: 18
Way back: 41
Finally: 54
"""

# Example: 18
# Result part 1, first attempt: 247
# Is right.
