#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
You climb the hill and again try contacting the Elves. However, you instead receive a signal you weren't expecting: a distress signal.

Your handheld device must still not be working properly; the packets from the distress signal got decoded out of order. You'll need to re-order the list of received packets (your puzzle input) to decode the message.

Your list consists of pairs of packets; pairs are separated by a blank line. You need to identify how many pairs of packets are in the right order.

For example:

[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]

Packet data consists of lists and integers. Each list starts with [, ends with ], and contains zero or more comma-separated values (either integers or other lists). Each packet is always a list and appears on its own line.

When comparing two values, the first value is called left and the second value is called right. Then:

    If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
    If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
    If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].

Using these rules, you can determine which of the pairs in the example are in the right order:

== Pair 1 ==
- Compare [1,1,3,1,1] vs [1,1,5,1,1]
  - Compare 1 vs 1
  - Compare 1 vs 1
  - Compare 3 vs 5
    - Left side is smaller, so inputs are in the right order

== Pair 2 ==
- Compare [[1],[2,3,4]] vs [[1],4]
  - Compare [1] vs [1]
    - Compare 1 vs 1
  - Compare [2,3,4] vs 4
    - Mixed types; convert right to [4] and retry comparison
    - Compare [2,3,4] vs [4]
      - Compare 2 vs 4
        - Left side is smaller, so inputs are in the right order

== Pair 3 ==
- Compare [9] vs [[8,7,6]]
  - Compare 9 vs [8,7,6]
    - Mixed types; convert left to [9] and retry comparison
    - Compare [9] vs [8,7,6]
      - Compare 9 vs 8
        - Right side is smaller, so inputs are not in the right order

== Pair 4 ==
- Compare [[4,4],4,4] vs [[4,4],4,4,4]
  - Compare [4,4] vs [4,4]
    - Compare 4 vs 4
    - Compare 4 vs 4
  - Compare 4 vs 4
  - Compare 4 vs 4
  - Left side ran out of items, so inputs are in the right order

== Pair 5 ==
- Compare [7,7,7,7] vs [7,7,7]
  - Compare 7 vs 7
  - Compare 7 vs 7
  - Compare 7 vs 7
  - Right side ran out of items, so inputs are not in the right order

== Pair 6 ==
- Compare [] vs [3]
  - Left side ran out of items, so inputs are in the right order

== Pair 7 ==
- Compare [[[]]] vs [[]]
  - Compare [[]] vs []
    - Right side ran out of items, so inputs are not in the right order

== Pair 8 ==
- Compare [1,[2,[3,[4,[5,6,7]]]],8,9] vs [1,[2,[3,[4,[5,6,0]]]],8,9]
  - Compare 1 vs 1
  - Compare [2,[3,[4,[5,6,7]]]] vs [2,[3,[4,[5,6,0]]]]
    - Compare 2 vs 2
    - Compare [3,[4,[5,6,7]]] vs [3,[4,[5,6,0]]]
      - Compare 3 vs 3
      - Compare [4,[5,6,7]] vs [4,[5,6,0]]
        - Compare 4 vs 4
        - Compare [5,6,7] vs [5,6,0]
          - Compare 5 vs 5
          - Compare 6 vs 6
          - Compare 7 vs 0
            - Right side is smaller, so inputs are not in the right order

What are the indices of the pairs that are already in the right order? (The first pair has index 1, the second pair has index 2, and so on.) In the above example, the pairs in the right order are 1, 2, 4, and 6; the sum of these indices is 13.

Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?
"""

"""
Lines start with [, end with ] (and are a single list, methinks).

Left is first line. shall be smaller. or shorter.

If both are integers (several digits!), smaller value to the left. So, if not same, break right or wrong.

If both are lists -- do that list. If contents match till end of list, shorter list is smaller. 

If one is integer and other list, expand integer to single-Item list. Compare lists from there.
"""

"""
Now, you just need to put all of the packets in the right order. Disregard the blank lines in your list of received packets.

The distress signal protocol also requires that you include two additional divider packets:

[[2]]
[[6]]

Using the same rules as before, organize all packets - the ones in your list of received packets as well as the two divider packets - into the correct order.

For the example above, the result of putting the packets in the correct order is:

[]
[[]]
[[[]]]
[1,1,3,1,1]
[1,1,5,1,1]
[[1],[2,3,4]]
[1,[2,[3,[4,[5,6,0]]]],8,9]
[1,[2,[3,[4,[5,6,7]]]],8,9]
[[1],4]
[[2]]
[3]
[[4,4],4,4]
[[4,4],4,4,4]
[[6]]
[7,7,7]
[7,7,7,7]
[[8,7,6]]
[9]

Afterward, locate the divider packets. To find the decoder key for this distress signal, you need to determine the indices of the two divider packets and multiply them together. (The first packet is at index 1, the second packet is at index 2, and so on.) In this example, the divider packets are 10th and 14th, and so the decoder key is 140.

Organize all of the packets into the correct order. What is the decoder key for the distress signal?
"""

"""
Do a sort of list + distress signals
Do a bubble sort:
Compare first to second, if order is wrong, switch around, 
optionally set "unfinished" bool -- the compare is expensive, so...
Compare second to third, ...
Until end of list. Next run -1, as last element is biggest of all.
Repeat until end counter is 0. Or "unfinished" is never set.
"""

lines = [ '[[2]]', '[[6]]' ]
index = 0 
switch = True

with open('Day13-Input', 'r') as file:
    for line in file:
        #print(line)
        if line == "\n":
            continue
        lines.append(line[:-1])

stop = len(lines)

while stop > 0 and switch:
    index = 0
    stop -= 1
    switch = False
    while stop > index:
        left = lines[index]
        right = lines[index+1]
        posl, posr = 0, 0
        order = ''
        while not order:
            if left[posl] == "]":
                if right[posr] == "]":
                    dummy = 1
                else:
                    # print("Finished. Right order. ],")
                    order = "right"
            elif left[posl] == ",":
                if right[posr] == "]":
                    # print("Finished. Wrong order. ,]")
                    order = "wrong"
                    switch = True
                else:
                    #print("Same. continue. ,,")
                    dummy = 1
            elif left[posl] == "[":
                if right[posr] == "[":
                    #print("Same. continue. [[")
                    dummy = 1
                elif right[posr] == "]":
                    # print("Finished. Wrong order. Right list is shorter.")
                    order = "wrong"
                    switch = True
                else:
                    # A number. make singleton list. And continue.
                    i = 1
                    #print("me here.", right[posr:])
                    while right[posr+i] not in ',]':
                        i += 1
                    right = "[" + right[posr:posr+i] + "]" + right[posr+i:]
                    posr = 0
                    #print("Appended right.", right[posr:])
                    #print("Made a list on right. [<int>")
            else: # A number on the left
                if right[posr] == "[":
                    # Make singleton list on left. Continue.
                    i = 1
                    while left[posl+i] not in ',]':
                        i += 1
                    left = "[" + left[posl:posl+i] + "]" + left[posl+i:]
                    posl = 0
                    #print("Made a list on left. <int>[")
                elif right[posr] == "]":
                    # print("Finished. Wrong order. <int>]")
                    order = "wrong"
                    switch = True
                else: # both are numbers
                    i = 1
                    while left[posl+i] not in ',]':
                        i += 1
                    cl = int(left[posl:posl+i])
                    posl += i - 1
                    i = 1
                    while right[posr+i] not in ',]':
                        i += 1
                    cr = int(right[posr:posr+i])
                    posr += i - 1
                    if cl < cr:
                        # print("Finished. Right order.", cl, cr)
                        order = "right"
                    elif cl > cr:
                        # print("Finished. Wrong order.", cl, cr)
                        order = "wrong"
                        switch = True
                    else: # equal
                        #print("Same. continue.", cl, cr)
                        dummy = 1
            posl += 1
            posr += 1
        if order == "wrong":
            h = lines[index]
            lines[index] = lines[index+1]
            lines[index+1] = h
        index += 1 


print(lines)
for i in range(len(lines)):
    if lines[i] == '[[2]]':
        out = i + 1
    elif lines[i] == '[[6]]':
        out *= (i + 1)

print()
print(out)

