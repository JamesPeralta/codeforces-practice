"""

all evens

OR 

all evens and an odd

2,2,2,1,3,5

3

6,2,4

cost to get them all even 

k - cost to get them even = r

if r is even we're good good
if r is odd say No

get them all to even.. Then it's a palindrome
Then look at remainder

"""

from collections import defaultdict
tests = int(input())

for _ in range(tests):

    first = input().split()
    k = int(first[1])
    count = defaultdict(int)
    second = input()
    for elem in second:
        count[elem] += 1
    

    odds = 0
    for elem in count:
        if count[elem] % 2 != 0:
            odds += 1
    
    """
    {
        a: 1
        b: 2
    }
    """
    # remove odds
    if k > 0:
        tmp = odds - k
        odds = max(0, tmp)
        k = abs(tmp)
    

    if odds == 1 or odds == 0:
        print("YES")
    else:
        print("NO")
