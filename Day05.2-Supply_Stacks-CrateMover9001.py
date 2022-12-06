#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?"""

initialised = False
init_stacks = []
stacks = []
lines = 0
out = ""

with open('Day05-Input', 'r') as file:
    for line in file:
        if line[0] == "m":
            # do the moves
            move = []
            dummy0, count, dummy1, source, dummy2, target = line.split()
            for i in range(int(count)):
                move.append(stacks[int(source)-1].pop())
            while move:
                stacks[int(target)-1].append(move.pop())
        elif line[0] == "[":
            # chop up line to stack_pre lists
            if initialised:
                lines += 1
                for i in range(no_cols):
                    init_stacks[i].append(line[i*4+1])
            else:
                no_cols = int(len(line) / 4)
                for i in range(no_cols):
                    init_stacks.append([line[i*4+1]])
                    stacks.append([])
                initialised = True
        elif line[0] == " ":
            # make the working stacks
            for i in range(no_cols):
                while init_stacks[i]:
                    fill_in = init_stacks[i].pop()
                    if fill_in != " ":
                        stacks[i].append(fill_in)

print(stacks)
for i in range(no_cols):
    out += stacks[i].pop()
print(out)

