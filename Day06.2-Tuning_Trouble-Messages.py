#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

    mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

How many characters need to be processed before the first start-of-message marker is detected?
"""

"""
Building on 6.1, this suggests reworking the checks therein to loop though all 14 elements. Using the simple cascading I used before would work, but ends up being way too much code. When done well, it may even handle the initialisation bits (building up the code to it's intended length. Plenty checks for < 0 ahead :)
"""

clear_at = 0
last13 = ""

with open('Day06-Input', 'r') as file:
    stream = file.read()

#stream = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"  # 19
#stream = "bvwbjplbgvbhsrlpgdmjqwftvncz"    # 23
#stream = "nppdvjthqldpwncqszvftbrmjlhg"    # 23
#stream = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"   # 29
#stream = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"    # 26

pos = 0
while pos < len(stream):
    next_one = stream[pos]
    last13 += next_one
    for i in range(13,-1,-1):
        #print(last14, clear_at, pos, i)
        if len(last13) - 2 < i:
            continue
        elif next_one == last13[i]:
            #print("Double: ", next_one) 
            cl_pos = pos - 13
            if cl_pos < 0:
                cl_pos = 0
            cl_pos +=i
            clear_at = max(clear_at, cl_pos)
    if clear_at < pos - 13: # this is it, then
        print(pos+1, last13)
        break
    if len(last13) > 13:
        last13 = last13[1:]
    pos +=1

