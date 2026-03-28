"""
3 6 3
14 9 11

n = 3
c = 6
k = 3

9

4, 11, 14
^

Ai <= 6



ans = 6
We're given ai
"""

tests = int(input())

for _ in range(tests):
    first = input().split()
    n = int(first[0])
    c = int(first[1])
    k = int(first[2])

    second = [int(elem) for elem in input().split()]
    second.sort()

    for num in second:
        if num <= c:
            diff = min(k, c - num)
            k -= diff

            c += (num + diff)
    print(c)

"""
diff = 4
k= 3
"""







