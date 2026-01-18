"""
6 3
n p | n is num residents and p = cost for pak to share
2 3 2 1 1 3 max they can share to
4 3 2 6 3 6 cost for each resident
    ^   ^ ^
1 2 3 4 5 6

Don't want to share to the same person twice because it's a waste

if the cost for pak to share is lower than resident, pak will just share the
message to the person with the lowest cost?

find the person who can spread the messsage the cheapest

if they can't share

2 3 2 1 1 3 max they can share to
4 3 2 6 3 6 cost for each resident
 c, share

[(2, 2), (3, 3), (3, 1), (3, 2), (3, 3), (3, 1)]

1
5 4
2 3 1 3 3
3 2 2 2 1

9
"""
num_cases = int(input())

for _ in range(num_cases):
    first = input().split()
    n, k = int(first[0]), int(first[1])
    second = [int(elem) for elem in input().split()] # can spread
    third = [int(elem) for elem in input().split()] # Cost

    arr = list(zip(third, second))
    arr = sorted(arr, key=lambda x: (x[0], x[1] * -1))
    arr = [list(elem) for elem in arr]

    cost = k
    curr = 0
    index = 1
    while index < len(arr):
        # leader sends the message
        # print(cost, curr, index)
        if k <= arr[curr][0]:
            cost += k
            index += 1
        else:
            while arr[curr][1] > 0 and index < len(arr):
                # print(cost, curr, index)
                cost += arr[curr][0]
                arr[curr][1] -= 1
                index += 1
            curr += 1
    
    print(cost)

"""
1
5 4
2 3 1 3 3
3 2 2 2 1
"""