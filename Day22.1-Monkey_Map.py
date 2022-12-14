#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
The monkeys take you on a surprisingly easy trail through the jungle. They're even going in roughly the right direction according to your handheld device's Grove Positioning System.

As you walk, the monkeys explain that the grove is protected by a force field. To pass through the force field, you have to enter a password; doing so involves tracing a specific path on a strangely-shaped board.

At least, you're pretty sure that's what you have to do; the elephants aren't exactly fluent in monkey.

The monkeys give you notes that they took when they last saw the password entered (your puzzle input).

For example:

        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5

The first half of the monkeys' notes is a map of the board. It is comprised of a set of open tiles (on which you can move, drawn .) and solid walls (tiles which you cannot enter, drawn #).

The second half is a description of the path you must follow. It consists of alternating numbers and letters:

    A number indicates the number of tiles to move in the direction you are facing. If you run into a wall, you stop moving forward and continue with the next instruction.
    A letter indicates whether to turn 90 degrees clockwise (R) or counterclockwise (L). Turning happens in-place; it does not change your current tile.

So, a path like 10R5 means "go forward 10 tiles, then turn clockwise 90 degrees, then go forward 5 tiles".

You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing to the right (from the perspective of how the map is drawn).

If a movement instruction would take you off of the map, you wrap around to the other side of the board. In other words, if your next tile is off of the board, you should instead look in the direction opposite of your current facing as far as you can until you find the opposite edge of the board, then reappear there.

For example, if you are at A and facing to the right, the tile in front of you is marked B; if you are at C and facing down, the tile in front of you is marked D:

        ...#
        .#..
        #...
        ....
...#.D.....#
........#...
B.#....#...A
.....C....#.
        ...#....
        .....#..
        .#......
        ......#.

It is possible for the next tile (after wrapping around) to be a wall; this still counts as there being a wall in front of you, and so movement stops before you actually wrap to the other side of the board.

By drawing the last facing you had with an arrow on each tile you visit, the full path taken by the above example looks like this:

        >>v#    
        .#v.    
        #.v.    
        ..v.    
...#...v..v#    
>>>v...>#.>>    
..#v...#....    
...>>>>v..#.    
        ...#....
        .....#..
        .#......
        ......#.

To finish providing the password to this strange input device, you need to determine numbers for your final row, column, and facing as your final position appears from the perspective of the original map. Rows start from 1 at the top and count downward; columns start from 1 at the left and count rightward. (In the above example, row 1, column 1 refers to the empty space with no tile on it in the top-left corner.) Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^). The final password is the sum of 1000 times the row, 4 times the column, and the facing.

In the above example, the final row is 6, the final column is 8, and the final facing is 0. So, the final password is 1000 * 6 + 4 * 8 + 0: 6032.

Follow the path given in the monkeys' notes. What is the final password?
"""

initmap = []
move = []
direction = []
minx = {}
maxx = {}
miny = {}
maxy = {}
prev_minx = 10000
for i in range(150):
    miny[i] = 10000
count = 0

#with open('Day22-Input--Debug', 'r') as file:
with open('Day22-Input', 'r') as file:
    for line in file:
        #print(len(line))
        if line[0].isdigit():
            n = ''
            for char in line:
                if char.isdigit():
                    n += char
                else:
                    move.append(int(n))
                    direction.append(char)
                    n = ''
            direction.pop()
        if line[0] in ' .#':
            for i in range(len(line)):
                if line[i] != ' ':
                    minx[count] = i
                    break
            for j in range(len(line)-1, i, -1):
                if line[j] != ' ':
                    maxx[count] = j
                    break
            for i in range(minx[count], maxx[count]):
                miny[i] = min(miny[i], count)
            if count and len(line) - 1 < len(initmap[-1]):
                for i in range(len(line)-1, len(initmap[-1])):
                    maxy[i] = count
            if minx[count] > prev_minx:
                for i in range(prev_minx, minx[count]):
                    maxy[i] = count
                               
            initmap.append(line.rstrip('\n'))
            prev_minx = minx[count]
            count += 1

for i in range(len(initmap[-1])):
    if initmap[-1][i] != ' ':
        maxy[i] = len(initmap)

print(move)
print(direction)
print(minx)
print(maxx)
print(miny)
print(maxy)

face = 'r'
posy = 0
posx = minx[posy] # not quite correct. first free tile is to be used. but.

for count in range(len(move)):
    mv = move[count]
    if face == 'r':
        for step in range(mv):
            if posx + 1 == maxx[posy]:
                if initmap[posy][minx[posy]] == '.':
                    posx = minx[posy]
                else:
                    break
            elif initmap[posy][posx+1] == '#':
                break
            else:
                posx += 1
    elif face == 'l':
        for step in range(mv):
            if posx - 1 < minx[posy]:
                if initmap[posy][maxx[posy]-1] == '.':
                    posx = maxx[posy] - 1
                else:
                    break
            elif initmap[posy][posx-1] == '#':
                break
            else:
                posx -= 1
    elif face == 'd':
        for step in range(mv):
            if posy + 1 == maxy[posx]:
                if initmap[miny[posx]][posx] == '.':
                    posy = miny[posx]
                else:
                    break
            elif initmap[posy+1][posx] == '#':
                break
            else:
                posy += 1
    elif face == 'u':
        for step in range(mv):
            if posy - 1 < miny[posx]:
                print("Moving up, wrap", posx, miny[posx], maxy[posx])
                if initmap[maxy[posx]-1][posx] == '.':
                    posy = maxy[posx] - 1
                else:
                    break
                posy = maxy[posx] - 1
            elif initmap[posy-1][posx] == '#':
                break
            else:
                posy -= 1
    if count == len(direction):
        break
    turn = direction[count]
    if turn == 'L':
        if face == 'r':
            face = 'u'
        elif face == 'u':
            face = 'l'
        elif face == 'l':
            face = 'd'
        else:
            face = 'r'
    else:
        if face == 'r':
            face = 'd'
        elif face == 'd':
            face = 'l'
        elif face == 'l':
            face = 'u'
        else:
            face = 'r'

if face == 'r':
    fp = 0
elif face == 'd':
    fp = 1
elif face == 'l':
    fp = 2
else:
    fp = 3

print(posy, posx, face)
print( (posy+1) * 1000 + (posx+1) * 4 + fp )

# Example: 6032
# Input: 131052 (130, 12, r)
