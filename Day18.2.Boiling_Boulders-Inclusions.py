#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
Something seems off about your calculation. The cooling rate depends on exterior surface area, but your calculation also included the surface area of air pockets trapped in the lava droplet.

Instead, consider only cube sides that could be reached by the water and steam as the lava droplet tumbles into the pond. The steam will expand to reach as much as possible, completely displacing any air on the outside of the lava droplet but never expanding diagonally.

In the larger example above, exactly one cube of air is trapped within the lava droplet (at 2,2,5), so the exterior surface area of the lava droplet is 58.

What is the exterior surface area of your scanned lava droplet?
"""

"""
Get range of each dimension,
for each point in each range, look if a bigger one exists and a smaller one exists. 
Also, do the 17.1 dance.
For all found, do the 17.1 dance again on that list.
Subtract the latter from the former.
"""

surface = 0
cubes = []
inclusions = []

minx = miny = minz = 100
maxx = maxy = maxz = 0

#with open('Day18-Input', 'r') as file:
with open('Day18-Input--Debug', 'r') as file:
    for line in file:
        x, y, z = line.strip().split(',')
        x = int(x)
        y = int(y)
        z = int(z)
        minx = min(minx, x)
        miny = min(miny, y)
        minz = min(minz, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
        maxz = max(maxz, z)
        cubes.append( (x, y, z ) )

for cube in cubes:
    s = 6
    x, y, z = cube[0], cube[1], cube[2]
    if (x-1, y, z) in cubes:
        s -= 1
    if (x+1, y, z) in cubes:
        s -= 1
    if (x, y-1, z) in cubes:
        s -= 1
    if (x, y+1, z) in cubes:
        s -= 1
    if (x, y, z-1) in cubes:
        s -= 1
    if (x, y, z+1) in cubes:
        s -= 1
    surface += s


for cx in range(minx, maxx+1):
    for cy in range(miny, maxy+1):
        for cz in range(minz, maxz+1):
            print("Testing", cx, cy, cz)
            if (cx, cy, cz) in cubes:
                print("Is in cubes")
                continue
            lower_x = False
            lower_y = False
            lower_z = False
            higher_x = False
            higher_y = False
            higher_z = False
            for i in range(minx, cx):
                if (i, cy, cz) in cubes:
                    lower_x = True
            for i in range(cx+1, maxx+1):
                if (i, cy, cz) in cubes:
                    higher_x = True
            for i in range(miny, cy):
                if (cx, i, cz) in cubes:
                    lower_y = True
            for i in range(cy+1, maxy+1):
                if (cx, i, cz) in cubes:
                    higher_y = True
            for i in range(minz, cz):
                if (cx, cy, i) in cubes:
                    lower_z = True
            for i in range(cz+1, maxz+1):
                if (cx, cy, i) in cubes:
                    higher_z = True
            if lower_x == higher_x == lower_y == higher_y == lower_z == higher_z == True:
                print("We've got an inclusion")
                inclusions.append( (cx,cy,cz) )

print(inclusions)
inner_surface = 0
for cube in inclusions:
    s = 6
    x, y, z = cube[0], cube[1], cube[2]
    if (x-1, y, z) in inclusions:
        s -= 1
    if (x+1, y, z) in inclusions:
        s -= 1
    if (x, y-1, z) in inclusions:
        s -= 1
    if (x, y+1, z) in inclusions:
        s -= 1
    if (x, y, z-1) in inclusions:
        s -= 1
    if (x, y, z+1) in inclusions:
        s -= 1
    inner_surface += s

print(surface)
print(inner_surface)

surface -= inner_surface

print(surface)

# 2576 is too low
# 58 is the example result.

