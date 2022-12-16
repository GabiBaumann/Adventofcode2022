#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves gave you. However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in these tunnels, and one of the elephants apparently figured out how to turn on the distress signal.

The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your handheld device; it reports mostly igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a cave, it's a volcano!

You need to get the elephants out of here, quickly. Your device estimates that you have 30 minutes before the volcano erupts, so you don't have time to go back out the way you came in.

You scan the cave for other options and discover a network of pipes and pressure-release valves. You aren't sure how such a system got into a volcano, but you don't have time to complain; your device produces a report (your puzzle input) of each valve's flow rate if it were opened (in pressure per minute) and the tunnels you could use to move between the valves.

There's even a valve in the room you and the elephants are currently standing in labeled AA. You estimate it will take you one minute to open a single valve and one minute to follow any tunnel from one valve to another. What is the most pressure you could release?

For example, suppose you had the following scan output:

Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II

All of the valves begin closed. You start at valve AA, but it must be damaged or jammed or something: its flow rate is 0, so there's no point in opening it. However, you could spend one minute moving to valve BB and another minute opening it; doing so would release pressure during the remaining 28 minutes at a flow rate of 13, a total eventual pressure release of 28 * 13 = 364. Then, you could spend your third minute moving to valve CC and your fourth minute opening it, providing an additional 26 minutes of eventual pressure release at a flow rate of 2, or 52 total pressure released by valve CC.

Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical. Instead, consider this approach:

== Minute 1 ==
No valves are open.
You move to valve DD.

== Minute 2 ==
No valves are open.
You open valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You move to valve CC.

== Minute 4 ==
Valve DD is open, releasing 20 pressure.
You move to valve BB.

== Minute 5 ==
Valve DD is open, releasing 20 pressure.
You open valve BB.

== Minute 6 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve AA.

== Minute 7 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve II.

== Minute 8 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve JJ.

== Minute 9 ==
Valves BB and DD are open, releasing 33 pressure.
You open valve JJ.

== Minute 10 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve II.

== Minute 11 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve AA.

== Minute 12 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve DD.

== Minute 13 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve EE.

== Minute 14 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve FF.

== Minute 15 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve GG.

== Minute 16 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve HH.

== Minute 17 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You open valve HH.

== Minute 18 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve GG.

== Minute 19 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve FF.

== Minute 20 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve EE.

== Minute 21 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve EE.

== Minute 22 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve DD.

== Minute 23 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve CC.

== Minute 24 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You open valve CC.

== Minute 25 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 27 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 28 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 29 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 30 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

This approach lets you release the most pressure possible in 30 minutes with this valve layout, 1651.

Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?
"""

"""
Do a recursion of possible paths, follow each to minute 30. Local maxima
won't help here, but recursion is limited to 30 - valves opened.

Nonono! Local minima help here. Brute Force takes waaay too long.
So do a local path minimization from one valve to all other working ones.

# Also, going back to a place already visited is fine.
Again, no, finding shortest path uses this.

Opening a valve with 0 rate (most of them) is useless.

Valves with rates > 0 may be turned or no. # The recursion should call itself for all possible routes twice: After opening or before.
Again, no, just jump from valve to valve for opening. 
Just computing the order isn't trivial: can be 29 x -- 27 or so x, so it's still better off iterated.

Keep track of rooms with valve already-open. This is the second condition when not to open a valve.

Organise input in a list of valve IDs being the name of dict with rate: int, path: list/tuple.
"""

def find_path(nowpos, target, step, maxsteps, visited): #maxsteps: min of maxsteps, tl. Needs to be >0.
    if target in vd[nowpos]['paths']:
        return step+1
    if step + 1 == maxsteps:
        return maxsteps
    visited.append(nowpos)
    for path in vd[nowpos]['paths']:
        if path in visited:
            continue
        steps = find_path(path, target, step+1, maxsteps, visited[:])
        maxsteps = min(maxsteps, steps)
    return maxsteps


def increaseflow(pos, tl, cf, sf, ov):
    """
    Find max flow within 30 minutes
    pos: current position
    tl: time left. return on zero.
    cf: current flow.
    sf: sum of flows. Increase by cf each minute.
    ov: list of open valves
    return sf when tl = 0
    """

    global mf
    #print('Now:', pos, tl, cf, sf, ov)
    if len(ov) == len(usablevalves):
        #print('Now just wait', ov)
        return sf + tl * cf

    for valve in usablevalves:
        if valve in ov:
            continue
        # get distance to valve
        print("Looking up", valve)
        step = 0
        minsteps = tl
        steps = find_path(pos, valve, step, minsteps, [])
        ntl = tl - (steps + 1)
        nsf = sf + (steps + 1) * cf
        ncf = cf + vd[valve]['rate']
        nov = ov[:] 
        nov.append(valve) # do that in param
        if ntl > 0:
            nsf = increaseflow(valve, ntl, ncf, nsf, nov[:])
        mf = max(mf, nsf)
    print("Returning increaseflow", mf)
    return nsf

minutes = 30
vd = {}
mf = 0
usablevalves = []

with open('Day16-Input--Debug', 'r') as file:
    for line in file:
        valvepath = []
        valveid = line.split()[1]
        valverate = int(line.split('=')[1].split(';')[0])
        if valverate > 0:
            usablevalves.append(valveid)
        for i in line.split()[9:]:
            valvepath.append(i.rstrip(','))
        vd[valveid] = {'rate': valverate, 'paths': valvepath}
        #print(vd[valveid]['rate'])

startpos = list(vd.keys())[0]
out = increaseflow(startpos, minutes, 0, 0, [])
print(out)
