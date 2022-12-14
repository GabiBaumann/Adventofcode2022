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

"""
As you reach the force field, you think you hear some Elves in the distance. Perhaps they've already arrived?

You approach the strange input device, but it isn't quite what the monkeys drew in their notes. Instead, you are met with a large cube; each of its six faces is a square of 50x50 tiles.

To be fair, the monkeys' map does have six 50x50 regions on it. If you were to carefully fold the map, you should be able to shape it into a cube!

In the example above, the six (smaller, 4x4) faces of the cube are:

        1111
        1111
        1111
        1111
222233334444
222233334444
222233334444
222233334444
        55556666
        55556666
        55556666
        55556666

You still start in the same position and with the same facing as before, but the wrapping rules are different. Now, if you would walk off the board, you instead proceed around the cube. From the perspective of the map, this can look a little strange. In the above example, if you are at A and move to the right, you would arrive at B facing down; if you are at C and move down, you would arrive at D facing up:

        ...#
        .#..
        #...
        ....
...#.......#
........#..A
..#....#....
.D........#.
        ...#..B.
        .....#..
        .#......
        ..C...#.

Walls still block your path, even if they are on a different face of the cube. If you are at E facing up, your movement is blocked by the wall marked by the arrow:

        ...#
        .#..
     -->#...
        ....
...#..E....#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

Using the same method of drawing the last facing you had with an arrow on each tile you visit, the full path taken by the above example now looks like this:

        >>v#
        .#v.
        #.v.
        ..v.
...#..^...v#
.>>>>>^.#.>>
.^#....#....
.^........#.
        ...#..v.
        .....#v.
        .#v<<<<.
        ..v...#.

The final password is still calculated from your final position and facing from the perspective of the map. In this example, the final row is 5, the final column is 7, and the final facing is 3, so the final password is 1000 * 5 + 4 * 7 + 3 = 5031.

Fold the map into a cube, then follow the path given in the monkeys' notes. What is the final password?
"""

"""
Wrap <-
y= 0 - 49, x = 50 and (moving left)
to y= 149 - 100, x=0  (moving right)

Wrap ->
y= 0-49, x = 149 and (moving right)
to y = 149 - 100, x=99 (moving left)

Wrap <-
y= 50-99, x=50 (moving left)
to x= 0-49, y= 100 (moving down)

Wrap ->
y= 50-99, x=99 (moving right)
to x= 100-149, y=49 (moving up)

Wrap <-
y= 100-149, x=0 (moving left)
to y= 49-0, x=50 (moving right)

Wrap ->
y= 100-149 x=99 (moving right)
to y= 49-0, x= 149 (moving left)

Wrap <-
y= 150-199, x=0 (moving left)
to x= 50-99, y=0 (moving down)

Wrap ->
y= 150-199, x=49 (moving right)
to x= 50-99, y=149 (moving up)

Wrap ^
x= 50-99, y=0 (moving up)
to y = 150-199, x=0 (moving right)

Wrap ^
x= 100-149, y=0 (moving up)
to x= 0-50, y = 199 (moving up)

Wrap v
x= 100-149, y=49 (moving down)
to y= 50-99, x=99 (moving left)

Wrap ^
x= 0-49, y=100 (moving up)
to y=50-99, x=50 (moving right)

Wrap v
x=50-99, y-149 (moving down)
to y= 150-199, x=49 (moving left)

Wrap v
x=0-49, y= 199 (moving down)
to x=100-149, y=0 (moving down)


I guess this can be done with algorithmic understanding of
cube topology giving a general solution,
to solve the example.
Transform into x/y/z coordinates, 
switching move in x dir on x/y plane to z motion on z/y plne?
Matrix transform to turn-on-wrap? Ewww...

So just go ahead and handle each wrap by the rules above...
When appending to list on wrap, that may not hurt too much.
Prolly start with modification to pop any action instruction from 0
and while loops instead of for loops.
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
count = 0

while count < len(move):
    continue_move = False
    mv = move[count]
    if face == 'r':
        print('Debug: Moving r', count, posx, posy, mv, face)
        for step in range(mv):
            if posx + 1 == maxx[posy]:
                if 0 <= posy < 50:
                    # continue at y: 149 - posy, x: 99 face: l (B)
                    # if there's no wall.
                    if initmap[149-posy][99] == '.':
                        posy = 149 - posy
                        posx = 99
                        face = 'l'
                        move[count] = mv - (step + 1)
                        # count -= 1 ## not needed, increment skipped by continue
                        continue_move = True # to skip direction...
                elif 50 <= posy < 100:
                    # continue at y: 49, x = posy + 50, face: 'u' (A)
                    if initmap[49][posy+50] == '.':
                        posx = posy + 50
                        posy = 49
                        face = 'u'
                        move[count] = mv - (step + 1)
                        continue_move = True
                elif 100 <= posy < 150:
                    # continue at y: 149-posy, x:149, face: l (B)
                    if initmap[149-posy][149] == '.':
                        posy = 149 - posy
                        posx = 149
                        face = 'l'
                        move[count] = mv - (step + 1)
                        continue_move = True
                elif 150 <= posy < 200:
                    # continue at y: 149, x: posy - 100, face: u (E)
                    if initmap[149][posy-100] == '.':
                        posx = posy - 100
                        posy = 149
                        face = 'u'
                        move[count] = mv - (step + 1)
                        continue_move = True
                break
            elif initmap[posy][posx+1] == '#':
                break
            else:
                posx += 1
    elif face == 'l':
        print('Debug: Moving l', count, posx, posy, mv, face, minx[posy])
        for step in range(mv):
            if posx - 1 < minx[posy]:
                if 0 <= posy < 50:
                    # continue at y: 149 - posy, x: 0, face: r (D)
                    if initmap[149-posy][0] == '.':
                        posy = 149 - posy
                        posx = 0
                        face = 'r'
                        move[count] = mv - (step + 1)
                        continue_move = True
                elif 50 <= posy < 100:
                    # continue at y: 100 , x: posy - 50 , face: d  (C)
                    if initmap[100][posy-50] == '.':
                        posx = posy - 50
                        posy = 100
                        face = 'd'
                        move[count] = mv - (step + 1)
                        continue_move = True
                elif 100 <= posy < 150:
                    # continue at y: 149 - posy, x: 50, face: r (D)
                    if initmap[149-posy][50] == '.':
                        posy = 149 - posy
                        posx = 50
                        face = 'r'
                        move[count] = mv - (step + 1)
                        continue_move = True
                elif 150 <= posy < 200:
                    # continue at y: 0, x: posy - 100, face: d  (F)
                    if initmap[0][posy-100] == '.':
                        posx = posy - 100
                        posy = 0
                        face = 'd'
                        move[count] = mv - (step + 1)
                        continue_move = True
                break
            elif initmap[posy][posx-1] == '#':
                break
            else:
                posx -= 1
    elif face == 'd':
        print('Debug: Moving d', count, posx, posy, mv, face)
        for step in range(mv):
            if posy + 1 == maxy[posx]:
                if 0 <= posx < 50:
                    # continue at y: 0, x: posx + 100 , face: d (G)
                    # direction remains, just set x, y and continue move
                    if initmap[0][posx+100] == '.':
                        posy = 0
                        posx = posx + 100
                        continue_move = False  #Required??
                        continue
                elif 50 <= posx < 100:
                    # continue at y: posx + 100, x: 49, face: l (E)
                    if initmap[posx+100][49] == '.':
                        posy = posx + 100
                        posx = 49
                        face = 'l'
                        move[count] = mv - (step + 1)
                        continue_move = True
                elif 100 <= posx < 150:
                    # continue at y: posx - 50, x: 99, face: l  (A)
                    if initmap[posx-50][99] == '.':
                        posy = posx - 50
                        posx = 99
                        face = 'l'
                        move[count] = mv - (step + 1)
                        continue_move = True
                break
            elif initmap[posy+1][posx] == '#':
                break
            else:
                posy += 1
    elif face == 'u':
        print('Debug: Moving u', count, posx, posy, mv, face)
        for step in range(mv):
            if posy - 1 < miny[posx]:
                if 0 <= posx < 50:
                    # continue at y: posx + 50, x: 50, face: r (C)
                    if initmap[posx+50][50] == '.':
                        posy = posx + 50
                        posx = 50
                        face= 'r'
                        move[count] = mv - (step + 1)
                        continue_move = True
                elif 50 <= posx < 100:
                    # continue at y: posx + 100, x: 0, face: r (F)
                    if initmap[posx+100][0] == '.':
                        posy = posx + 100
                        posx = 0
                        face = 'r'
                        move[count] = mv - (step + 1)
                        continue_move = True
                elif 100 <= posx < 150:
                    # continue at y: 199 , x: posx - 100, face: u (G)
                    # direction remains, just re-x,y and continue
                    if initmap[199][posx-100] == '.':
                        posy = 199
                        posx = posx - 100
                        continue_move = False ## Required?
                        continue
                break
            elif initmap[posy-1][posx] == '#':
                break
            else:
                posy -= 1
    if continue_move:
        continue
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
    count += 1

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

# 3 143 l (4k+144*4+2
# 4578

