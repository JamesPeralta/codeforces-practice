# Pattern: Case analysis — winner determined by first and last character of the turn string (both 0 → BOB, else ALICE)
"""
intuition.

can we turn the array into all 1s? or is it already all 1s?

if first and last == 1 -> ALIce

if first = 0 and last == 1

if first = 1 and last ==0 

0 0
"""

test_cases = int(input())

for i in range(test_cases):
    _ = input()
    turns = input()

    if turns[0] == "0" and turns[-1] == "0":
        print("BOB")
    else:
        print("ALICE")