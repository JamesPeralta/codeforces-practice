# Pattern: Memoization / DP — recursively split n into floor(n/2) and ceil(n/2); min steps to reach k is 1 + min(steps from first, steps from second); cache by n
test_cases = int(input())
import math

def recurse(n, k, cache):
    first = math.floor(n / 2)
    second = math.ceil(n / 2)
    if first == 0 or second == 0:
        return float("inf")
    
    if first == k or second == k:
        return 1

    if n in cache:
        return cache[n]

    cache[n] = min(recurse(first, k, cache), recurse(second, k, cache)) + 1
    # print(n)
    return cache[n]

for i in range(test_cases):
    line = input().split()
    n = int(line[0])
    k = int(line[1])
    if n == k:
        print(0)
    else:
        cache = {}
        result = recurse(n, k, cache)
        if result == float("inf"):
            print(-1)
        else:
            print(result)