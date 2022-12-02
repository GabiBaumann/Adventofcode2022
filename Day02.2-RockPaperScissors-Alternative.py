#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
"""

score = 0

with open('Day02-Input', 'r') as file:
    for line in file:
        elf = line[0]
        task = line[2]

        if elf == 'A':
            if task == 'X':
                # lose: pick Scissors < Rock
                score += 3
            elif task == 'Y':
                # draw: pick Rock = Rock
                score += 4
            else:
                # win: pick Paper > Rock
                score += 8
        elif elf == 'B':
            if task == 'X':
                # lose: pick Rock < Paper
                score += 1
            elif task == 'Y':
                # draw: pick Paper = Paper
                score += 5
            else:
                # win: pick Scissors > Paper
                score += 9
        else:
            if task == 'X':
                # lose: pick Paper < Scissors
                score += 2
            elif task == 'Y':
                # draw: pick Scissors = Scissors
                score += 6
            else:
                # win: pick Rock > Scissors
                score += 7

print(score)

