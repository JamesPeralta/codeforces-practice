"""
Prompt:

Andrei has a huge pile of n apples.

In one operation, he can divide a pile into two smaller piles:
- If a pile contains x apples, it splits into two piles of sizes
    ⌊x / 2⌋ and ⌈x / 2⌉.
- Each division takes 1 minute.

Andrei wants to eat exactly k apples, but he does not want to count apples individually.
Instead, he wants to obtain a pile that contains exactly k apples by repeatedly splitting piles.

For each test case, output -1 if it is impossible to obtain a pile with exactly k apples.
Otherwise, output the minimum possible time required to obtain such a pile.


example 1)
in = 10 3
out = 2

example 2)
in = 11 5
out = 1

example 3)
in = 21 4
out = -1

example 4)
in = 1000000000 1
out = 29
"""