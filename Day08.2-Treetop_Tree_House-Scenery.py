#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

30373
25512
65332
33549
35390

    Looking up, its view is not blocked; it can see 1 tree (of height 3).
    Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
    Looking right, its view is not blocked; it can see 2 trees.
    Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

30373
25512
65332
33549
35390

    Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
    Looking left, its view is not blocked; it can see 2 trees.
    Looking down, its view is also not blocked; it can see 1 tree.
    Looking right, its view is blocked at 2 trees (by a massive tree of height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?
"""

"""
So now, count down to left and up / count up for right and down and compare one by one until tree >= current tree. Can't be a border tree, they all have 0 scenery...
Multiply the four scores. (Never mind which tree that is.)
Get max of the scores.
"""

wood = []
max_scenery = 0

with open('Day08-Input', 'r') as file:
    for line in file:
        row =[]
        for char in line.rstrip():
            row.append(char)
        wood.append(row)

xmax = len(row) - 1
ymax = len(wood) - 1

for y in range(1, ymax):
    for x in range(1,xmax):
        th = wood[y][x]
        scenery = 1
        s = 1
        for i in range(x-1, 0, -1):
            if th <= wood[y][i]:
                break
            s += 1
        scenery *= s
        s = 1
        for i in range(x+1, xmax):
            if th <= wood[y][i]:
                break
            s += 1
        scenery *= s
        s = 1
        for i in range(y-1, 0, -1):
            if th <= wood[i][x]:
                break
            s += 1
        scenery *= s
        s = 1
        for i in range(y+1, ymax):
            if th <= wood[i][x]:
                break
            s += 1
        scenery *= s
        max_scenery = max(max_scenery, scenery)

print("Max scenic score: ", max_scenery)
