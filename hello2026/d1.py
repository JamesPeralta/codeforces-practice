test_cases = int(input())
from collections import defaultdict, deque

for i in range(test_cases):
    num_nodes = int(input())
    adj_list = defaultdict(set)
    for _ in range(num_nodes - 1):
        elem = input().split()
        # print(elem)
        i = int(elem[0])
        j = int(elem[1])
        adj_list[i].add(j)
        adj_list[j].add(i)
    
    # (node, depth)
    colored = set()
    turns = 0
    while len(colored) != num_nodes:
        seen_row = set()
        seen = set([1])
        just_colored = set()
        stack = [(1, 0)]
        while stack:
            node, depth = stack.pop()

            # For coloring
            neighbs_just_colored = False
            for neighb in adj_list[node]:
                if neighb in just_colored:
                    neighbs_just_colored = True
            if node not in colored and depth not in seen_row and neighbs_just_colored is False:
                # print("Turn ", turns, " Coloring ", node, just_colored)
                colored.add(node)
                just_colored.add(node)
                seen_row.add(depth)

            for neighb in adj_list[node]:
                if neighb in seen:
                    continue
                stack.append((neighb, depth + 1))
                seen.add(neighb)

        turns += 1
    print(turns)
"""
1
13
2 1
3 2
4 2
5 4
6 3
7 1
8 5
9 6
10 4
11 7
12 8
13 10

1
3
4

1, 4


1, 1, 3 -> 4
^
   ^

1, 3, 1 -> 4

2, 3, 2 -> 5

Deduce this to an array

Make array go to 0s..

Double for loop that

0, 4, 2

Evens = what's the max
Odds = what's the max

Evens_m + Odds_m

5
4
4
3
3
3
4
4
4
3

"""