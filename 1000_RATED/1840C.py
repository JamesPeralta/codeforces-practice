"""
n days for vacation

wants to go for consecutive days

only at least k days

q degrees.

input

1
3 1 15
-5 0 -10
3 days 
at least 1 day
has to be less than 15

-5 16 0 -10
        ^
      l
   r

5
1  2  3
-5 0 -10
      ^

equation to get # of contig of len > x
if given contig array.

1,3
X X X X X
^
        ^

Track sequence.. 
add 1 then 2 then 3 to the result for every number >= k for a seq
"""
tests = int(input())

for _ in range(tests):
    first = input().split()
    second = input()
    n, k, q = int(first[0]), int(first[1]), int(first[2])
    second = [int(i) for i in second.split()]

    result = 0
    seq = 0
    curr_multiplier = 0
    for i in range(len(second)):
        if second[i] > q:
            seq = 0
            curr_multiplier = 0
            continue

        seq += 1
        if seq >= k:
            curr_multiplier += 1
            result += curr_multiplier    

    print(result)