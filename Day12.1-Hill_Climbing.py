#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?
"""

"""
This is about path optimisation.
Do the next step recursively, trying each direction at any step.
Output minimum steps taken.

Record the ordinal values (shifted - 96) in the first place. Start with '`' (96) as character before 'a', end with '{' (123) as character after 'z'. At height 27: we've found one way to go.

This solution needs an array to keep track of how many steps it took to get to this position. If it gets there faster, set value to current number of steps.
"""

from sys import setrecursionlimit

def nextstep(cx,cy,h,s):
    """
    Recurse through all fields.
    cx: current x position
    cy: current y position
    h: current height
    s: number of steps taken
    """

    if ms[cy][cx] <= s:
        return
    ms[cy][cx] = s
    if h == 27:
        print("Got a solution: ", cx, cy, h, s)
        global minsteps
        if s < minsteps:
            minsteps = s
        return
    if cy - 1 >= 0 and m[cy-1][cx] <= h+1:
        nextstep(cx, cy-1, m[cy-1][cx], s+1)
    if cx - 1 >= 0 and m[cy][cx-1] <= h+1:
        nextstep(cx-1, cy, m[cy][cx-1], s+1)
    if cy + 1 < mheight and m[cy+1][cx] <= h+1:
        nextstep(cx, cy+1, m[cy+1][cx], s+1)
    if cx + 1 < mwidth and m[cy][cx+1] <= h+1:
        nextstep(cx+1, cy, m[cy][cx+1], s+1)
    return

m = []
ms = []
setrecursionlimit(10000)

with open('Day12-Input', 'r') as file:
    for line in file:
        ml = []
        for char in line.rstrip():
            if char == 'S':
                posx = len(ml)  ## Start (x)
                posy = len(m)   ## Start (y) 
                char = '`'
            elif char == 'E':
                char = '{'
            ml.append(ord(char) - 96)
        m.append(ml)

mheight = len(m)
mwidth = len(ml)
minsteps = mheight * mwidth
for y in range(mheight):
    ms.append([])
    for x in range(mwidth):
        ms[y].append(minsteps)

nextstep(posx, posy, 0, 0)  # x, y, height, steps taken

print("Min steps:", minsteps)

# 484 for 12.1 (in 5.5s)