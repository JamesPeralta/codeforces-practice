import sys
input = sys.stdin.readline
tests = int(input())

for _ in range(tests):
    first = ["2"] * int(input())
    _ = input()
    
    if len(first) == 1:
        print("1")
    else:
        print(" ".join(first))



"""
n chairs in a row - all unmarked.

Given some permutation of n.

Visit each chair sequentially, starting from the 1st char.
 - if ith is marked, end the game immediately.
 - Otherwise, sit on the chair and skip it and move to the next chair.
 - if you choose to sit than it's over

Figure out the maximum number of chairs you can sit on.


Observations:
- If the perm is less than or equal you're index.. It doesn't affect anything.
- if greater, sets a hard cap

"""