#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
Your handheld device has located an alternative exit from the cave for you and the elephants. The ground is rumbling almost continuously now, but the strange valves bought you some time. It's definitely getting warmer in here, though.

The tunnels eventually open into a very tall, narrow chamber. Large, oddly-shaped rocks are falling into the chamber from above, presumably due to all the rumbling. If you can't work out where the rocks will fall next, you might be crushed!

The five types of rocks have the following peculiar shapes, where # is rock and . is empty space:

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

The rocks fall in the order shown above: first the - shape, then the + shape, and so on. Once the end of the list is reached, the same order repeats: the - shape falls first, sixth, 11th, 16th, etc.

The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls themselves. A quick scan reveals the effect the jets of hot gas will have on the rocks as they fall (your puzzle input).

For example, suppose this was the jet pattern in your cave:

>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>

In jet patterns, < means a push to the left, while > means a push to the right. The pattern above means that the jets will push a falling rock right, then right, then right, then left, then left, then right, and so on. If the end of the list is reached, it repeats.

The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

After a rock appears, it alternates between being pushed by a jet of hot gas one unit (in the direction indicated by the next symbol in the jet pattern) and then falling one unit down. If any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does not occur. If a downward movement would have caused a falling rock to move into the floor or an already-fallen rock, the falling rock stops where it is (having landed on something) and a new rock immediately begins falling.

Drawing falling rocks with @ and stopped rocks with #, the jet pattern in the example above manifests as follows:

The first rock begins falling:
|..@@@@.|
|.......|
|.......|
|.......|
+-------+

Jet of gas pushes rock right:
|...@@@@|
|.......|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
+-------+

Jet of gas pushes rock left:
|..@@@@.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|..####.|
+-------+

A new rock begins falling:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|...@...|
|..@@@..|
|...@...|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|..####.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

A new rock begins falling:
|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

The moment each of the next few rocks begins falling, you would see this:

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|..#....|
|..#....|
|####...|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|..#....|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|.....#.|
|.....#.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|....##.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|##..##.|
|######.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

To prove to the elephants your simulation is accurate, they want to know how tall the tower will get after 2022 rocks have stopped (but before the 2023rd rock begins falling). In this example, the tower of rocks will be 3068 units tall.

How many units tall will the tower of rocks be after 2022 rocks have stopped falling?
"""

"""
Define the cave and rock coordinates bottom-up, so y=0 is the initial floor.

Floor is a bit tricky. Consider fallen rocks part of the floor,
represent floor as tuples in a list.
Just using max(y) won't do. 

I think it may not make sense to go for a ruleset to reduce floor space?
"""

"""
The elephants are not impressed by your simulation. They demand to know how tall the tower will be after 1000000000000 rocks have stopped! Only then will they feel confident enough to proceed through the cave.

In the example above, the tower would be 1514285714288 units tall!

How tall will the tower be after 1000000000000 rocks have stopped?
"""

"""
Now reducing floor space is needed to get to a solution in any useful time.
Can I go for minimum of maximum floor heights?
Not really, but it might just work.

Or even: cut off space x below floormax for a reasonably large x.

Otherwise, check for an unbroken path from left to right...
"""

rockmax = 2022
rockmax = 1000000000000

roomwidth = 7
xoff = 2
yoff = 3
floormax = 0
floormin = 0 # for reducing depth of the pile
floorbuffer = 100
floor = []
for i in range(roomwidth):
    floor.append( (i,0) )
rocktotal = 0

rocks = []
rockwidths = []
# Rock ####
rocks.append( ((0,0), (1,0), (2,0), (3,0)) )
rockwidths.append(4)
#       #
#      ###
# Rock  #   (1,1) cannot ever change anything, leave out
rocks.append( ((1,0), (0,1), (2,1), (1,2)) )
rockwidths.append(3)
#        #
#        #
# Rock ###
rocks.append( ((0,0), (1,0), (2,0), (2,1), (2,2)) )
rockwidths.append(3)
#      #
#      #
#      #
# Rock #
rocks.append( ((0,0), (0,1), (0,2), (0,3)) )
rockwidths.append(1)
#      ##
# Rock ##
rocks.append( ((0,0), (1,0), (0,1), (1,1)) )
rockwidths.append(2)

rockno = 0 # current number in loop(len(rocks))
rlooplen = len(rocks)

with open('Day17-Input--Debug', 'r') as file:
    line = file.read()
    line = line.rstrip()

linepos = 0
llooplen = len(line)

while rocktotal < rockmax:
    if rocktotal % 1000000 == 0:

        print("Now", rocktotal)
    rock = rocks[rockno]
    rockwidth = rockwidths[rockno]
    rocktotal += 1
    rockno += 1
    if rockno == rlooplen:
        rockno = 0
    xpos = xoff
    ypos = floormax + yoff + 1
    settled = False
    while not settled:
        jet = line[linepos]
        linepos += 1
        if linepos == llooplen:
            linepos = 0
        if jet == '<':
            #print("Jet <")
            if xpos > 0: # OR colliding
                if ypos > floormax:
                    xpos -= 1
                else:
                    can_move = True
                    for tile in rock:
                        x, y = tile[0], tile[1]
                        check = (xpos+x-1, ypos + y)
                        if check in floor:
                            can_move = False
                    if can_move:
                        xpos -= 1
                #print("Moves right", xpos,ypos)
        else:
            #print("Jet >")
            if xpos + rockwidth < roomwidth: # OR colliding
                if ypos > floormax:
                    xpos += 1
                else:
                    can_move = True
                    for tile in rock:
                        x, y = tile[0], tile[1]
                        check = (xpos+x+1, ypos+y)
                        if check in floor:
                            can_move = False
                    if can_move:
                        xpos += 1
                #print("Moves left", xpos, ypos)
        # now move down
        if ypos > floormax+1:
            ypos -=1
        else:
            for tile in rock:
                x, y = tile[0], tile[1]
                check = (xpos+x, ypos+y-1) # err, -1? depends...
                #print(check)
                if check in floor:
                    # Landed
                    settled = True
                    break
            if settled:
                # append to floor
                for tile in rock:
                    x, y = tile[0], tile[1]
                    floor.append( (xpos+x, ypos+y) )
                    floormax = max(floormax, ypos+y)
                #print(floormax, floor)
                # Reduce floor space
                print("Reducing floor space", floormax, floormin)
                if floormax > floormin + 2 * floorbuffer: # do a pile at once
                    floormin = floormax - floorbuffer
                    while True:
                        delme = list.pop(0)
                        if delme[1] > floormin:
                            break

            else:
                ypos -= 1

#print(floor)
print(floormax)

# 3090 for 17.1
