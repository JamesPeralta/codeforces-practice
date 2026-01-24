"""
There are thousands of 
{
 1: 1
 2: 1
 3: 2
 5: 1
}

1 2 3 3 5
  ^

Take the first array and find the max you can get from each
and store in a hashmap
4 5 5 3 3 6
    ^

Go through this array and for each consecutive you count and see the
longest it can be in the other and take the max of all of those results
"""
tests = int(input())
from collections import defaultdict

for b in range(tests):
    _ = input()
    first = [int(elem) for elem in input().split()]
    second = [int(elem) for elem in input().split()]

    sizes = defaultdict(int)
    curr_size = 1
    for i in range(len(first)):
        if i > 0 and first[i] == first[i - 1]:
            curr_size += 1
        else:
            curr_size = 1
        sizes[first[i]] = max(sizes[first[i]], curr_size)

    # print(sizes)
    result = max([v for _, v in sizes.items()])
    curr_size = 1
    # print(sizes)
    for i in range(len(second)):
        if i > 0 and second[i] == second[i - 1]:
            curr_size += 1
        else:
            curr_size = 1
        result = max(result, curr_size + sizes[second[i]])

    print(result)


"""
1
6
2 2 1 2 2 1
2 2 1 2 2 1
"""