# Pattern: Longest consecutive subsequence — sort unique values, scan for longest run where a[i] == a[i-1] + 1; answer is length of longest run
tests = int(input())

for _ in range(tests):
    first = input()
    second = list(set([int(elem) for elem in input().split()]))
    second.sort()
    # second = list(filter(lambda x: x >= 0, second))
    longest = 1
    curr = 1
    for i in range(1, len(second)):
        if second[i] == second[i -1] + 1:
            curr += 1
        else:
            curr = 1
        
        longest = max(longest, curr)

    # print(second)
    # dist_from_zero = second[0]
    # for i in range(len(second)):
    #     second[i] -= dist_from_zero

    # mex = 0
    # for i in range(len(second)):
    #     if second[i] == mex:
    #         mex += 1
    
    print(longest)
"""
1
5
2 4 1 0 -1
"""