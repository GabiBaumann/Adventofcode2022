#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
Your scans show that the lava did indeed form obsidian!

The wind has changed direction enough to stop sending lava droplets toward you, so you and the elephants exit the cave. As you do, you notice a collection of geodes around the pond. Perhaps you could use the obsidian to create some geode-cracking robots and break them open?

To collect the obsidian from the bottom of the pond, you'll need waterproof obsidian-collecting robots. Fortunately, there is an abundant amount of clay nearby that you can use to make them waterproof.

In order to harvest the clay, you'll need special-purpose clay-collecting robots. To make any type of robot, you'll need ore, which is also plentiful but in the opposite direction from the clay.

Collecting ore requires ore-collecting robots with big drills. Fortunately, you have exactly one ore-collecting robot in your pack that you can use to kickstart the whole operation.

Each robot can collect 1 of its resource type per minute. It also takes one minute for the robot factory (also conveniently from your pack) to construct any type of robot, although it consumes the necessary resources available when construction begins.

The robot factory has many blueprints (your puzzle input) you can choose from, but once you've configured it with a blueprint, you can't change it. You'll need to work out which blueprint is best.

For example:

Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.

(Blueprints have been line-wrapped here for legibility. The robot factory's actual assortment of blueprints are provided one blueprint per line.)

The elephants are starting to look hungry, so you shouldn't take too long; you need to figure out which blueprint would maximize the number of opened geodes after 24 minutes by figuring out which robots to build and when to build them.

Using blueprint 1 in the example above, the largest number of geodes you could open in 24 minutes is 9. One way to achieve that is:

== Minute 1 ==
1 ore-collecting robot collects 1 ore; you now have 1 ore.

== Minute 2 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.

== Minute 3 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
The new clay-collecting robot is ready; you now have 1 of them.

== Minute 4 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
1 clay-collecting robot collects 1 clay; you now have 1 clay.

== Minute 5 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
1 clay-collecting robot collects 1 clay; you now have 2 clay.
The new clay-collecting robot is ready; you now have 2 of them.

== Minute 6 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
2 clay-collecting robots collect 2 clay; you now have 4 clay.

== Minute 7 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
2 clay-collecting robots collect 2 clay; you now have 6 clay.
The new clay-collecting robot is ready; you now have 3 of them.

== Minute 8 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
3 clay-collecting robots collect 3 clay; you now have 9 clay.

== Minute 9 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
3 clay-collecting robots collect 3 clay; you now have 12 clay.

== Minute 10 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
3 clay-collecting robots collect 3 clay; you now have 15 clay.

== Minute 11 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 2 ore.
3 clay-collecting robots collect 3 clay; you now have 4 clay.
The new obsidian-collecting robot is ready; you now have 1 of them.

== Minute 12 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
3 clay-collecting robots collect 3 clay; you now have 7 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
The new clay-collecting robot is ready; you now have 4 of them.

== Minute 13 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 11 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.

== Minute 14 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 15 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 3 obsidian.

== Minute 15 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
4 clay-collecting robots collect 4 clay; you now have 5 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 4 obsidian.
The new obsidian-collecting robot is ready; you now have 2 of them.

== Minute 16 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 9 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.

== Minute 17 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 13 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.

== Minute 18 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 17 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 3 obsidian.
The new geode-cracking robot is ready; you now have 1 of them.

== Minute 19 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 21 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 5 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 1 open geode.

== Minute 20 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
4 clay-collecting robots collect 4 clay; you now have 25 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 7 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.

== Minute 21 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 29 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 2 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 3 open geodes.
The new geode-cracking robot is ready; you now have 2 of them.

== Minute 22 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
4 clay-collecting robots collect 4 clay; you now have 33 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 5 open geodes.

== Minute 23 ==
1 ore-collecting robot collects 1 ore; you now have 5 ore.
4 clay-collecting robots collect 4 clay; you now have 37 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 7 open geodes.

== Minute 24 ==
1 ore-collecting robot collects 1 ore; you now have 6 ore.
4 clay-collecting robots collect 4 clay; you now have 41 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 9 open geodes.

However, by using blueprint 2 in the example above, you could do even better: the largest number of geodes you could open in 24 minutes is 12.

Determine the quality level of each blueprint by multiplying that blueprint's ID number with the largest number of geodes that can be opened in 24 minutes using that blueprint. In this example, the first blueprint has ID 1 and can open 9 geodes, so its quality level is 9. The second blueprint has ID 2 and can open 12 geodes, so its quality level is 24. Finally, if you add up the quality levels of all of the blueprints in the list, you get 33.

Determine the quality level of each blueprint using the largest number of geodes it could produce in 24 minutes. What do you get if you add up the quality level of all of the blueprints in your list?
"""

"""
Another recursion. 
Can be run while reading input. But.

Ore and clay bots use one ingredient, ore, 
obsidian and geode bots use two (ore, clay) and (ore, obsidian) in each recipe.

The attempt at a brute-force recursion takes way to long.
So now: Save up for any bot whose ingredients are being mined.
Recurse over bots built.
"""

from copy import copy as cp

def buildbot(r,tl, bots, resources):
    "Build any bot if at all possible, recurse."
    #can_build = False
    maxgeodes = 0
    # ore bot (always possible)
    ore_needed = r['ore']['ore']
    duration = (ore_needed - resources['ore']) // bots['ore'] + 1
    if (ore_needed - resources['ore']) % bots['ore']:
        duration += 1
    if duration < 1:
        duration = 1
    if duration < tl:
        #can_build = True
        pass_res = cp(resources)
        for i in pass_res:
            pass_res[i] += bots[i] * duration
        pass_res['ore'] -= ore_needed
        pass_bots = cp(bots)
        pass_bots['ore'] += 1
        geodes = buildbot(r, tl-duration, pass_bots, pass_res)
        maxgeodes = max(maxgeodes, geodes)
    # clay bot (always possible)
    ore_needed = r['ore']['ore']
    duration = (ore_needed - resources['ore']) // bots['ore'] + 1
    if (ore_needed - resources['ore']) // bots['ore']:
        duration += 1
    if duration < 1:
        duration = 1
    if duration < tl:
        pass_res = cp(resources)
        for i in pass_res:
            pass_res[i] += bots[i] * duration
        pass_res['ore'] -= ore_needed
        pass_bots = cp(bots)
        pass_bots['clay'] += 1
        geodes = buildbot(r,tl-duration, pass_bots, pass_res)
        maxgeodes = max(maxgeodes, geodes)
    # obsidian bot
    if bots['clay']:
        ore_needed = r['obsidian']['ore']
        clay_needed = r['obsidian']['clay']
        d1 = (ore_needed - resources['ore']) // bots['ore'] + 1
        if (ore_needed - resources['ore']) % bots['ore']:
            d1 += 1
        d2 = (clay_needed - resources['clay']) // bots['clay'] + 1
        if (clay_needed - resources['clay']) % bots['clay']:
            d2 += 1
        duration = max(d1, d2)
        if duration < 1:
            duration = 1
        if duration < tl:
            pass_res = cp(resources)
            for i in pass_res:
                pass_res[i] += bots[i] * duration
            pass_res['ore'] -= ore_needed
            pass_res['clay'] -= clay_needed
            pass_bots = cp(bots)
            pass_bots['obsidian'] += 1
            geodes = buildbot(r, tl-duration, pass_bots, pass_res)
            maxgeodes = max(maxgeodes, geodes)
    # geode bot
    if bots['obsidian']:
        ore_needed = r['geode']['ore']
        obs_needed = r['geode']['obsidian']
        d1 = (ore_needed - resources['ore']) // bots['ore'] + 1
        if (ore_needed - resources['ore']) % bots['ore']:
            d1 += 1
        d2 = (obs_needed - resources['obsidian']) // bots['obsidian'] + 1
        if (obs_needed - resources['obsidian']) % bots['obsidian']:
            d2 += 1
        duration = max(d1, d2)
        if duration < 1:
            duration = 1
        if duration < tl:
            pass_res = cp(resources)
            for i in pass_res:
                pass_res[i] += bots[i] * duration
            pass_res['ore'] -= ore_needed
            pass_res['obsidian'] -= obs_needed
            pass_bots = cp(bots)
            pass_bots['geode'] += 1
            geodes = buildbot(r, tl-duration, pass_bots, pass_res)
            maxgeodes = max(maxgeodes, geodes)

    return resources['geode'] + maxgeodes + bots['geode'] * tl


minutes = 24
bots = { 'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
resources = { 'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}

recipes = []
maxgeodes = 0

with open('Day19-Input--Debug', 'r') as file:
    for line in file:
        recipe = {}
        blueprint, line = line.rstrip('.\n').split(':')
        blueprint = blueprint[-1]
        for item in line.split('.'):
            robot, costs = item.split('costs')
            robot = robot.split()[1]
            recipe[robot] = {}
            for cost in costs.split('and'):
                number, material = cost.split()
                recipe[robot][material] = int(number)
        recipes.append(recipe)

print(recipes)

i = 0
ql = 0
for r in recipes:
    # recources mined in this round
    i += 1
    geodes = buildbot(r, minutes, cp(bots), cp(resources)) # cp not needed
    print("Full run", geodes)
    ql += i * geodes
    maxgeodes = max(maxgeodes, geodes)

print(maxgeodes)
print(ql)
