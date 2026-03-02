import sys
input = sys.stdin.readline
tests = int(input())

for _ in range(tests):
    first = input().split()
    x = int(first[1])
    y = int(first[2]) 
    nums = [int(elem) for elem in input().split()]

    inside = []
    outside = []
    for i in range(len(nums)):
        if i < x:
            outside.append(nums[i])
        elif i >= y:
            outside.append(nums[i])
        else:
            inside.append(nums[i])
    
    # print(inside)
    # print(outside)
    min_inside = inside.index(min(inside))
    min_val = min(inside)
    new_inside = inside[min_inside:] + inside[:min_inside]
    
    res = []
    index_o = 0
    while index_o < len(outside):
        if outside[index_o] <= min_val:
            res.append(outside[index_o])
        else:
            break

        index_o += 1
    
    res += new_inside
    while index_o < len(outside):
        res.append(outside[index_o])
        index_o += 1
    
    print(" ".join([str(elem) for elem in res]))

"""
1
3 1 2
3 2 1
"""