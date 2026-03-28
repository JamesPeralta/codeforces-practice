import sys
input = sys.stdin.readline
tests = int(input())

for _ in range(tests):
    first = input().split()
    x = int(first[0])
    y = int(first[1])

    diff = abs(x - y)
    wyn = []
    while x > 0 and y > 0:
        x -= 1
        y -= 1
        wyn.append("1")
        wyn.append("-1")

    while x > 0:
        wyn.append("1")
        x -= 1
    
    while y > 0:
        wyn.append("-1")
        y -= 1

    res = 1
    while diff % 2 == 0 and diff != 0:
        res += 1
        diff = diff // 2
        # print(diff)
    print(res % 676767677)
    print(" ".join(wyn))


"""
Given x and y

Find the min value of f(a) over all arrays a

of length x + y

x copies of 1
and y copies of -1

If x = y return 1

x + 1, y

1, 1, -1

match them up.

6 7

1
-1 1 -1 1 -1 1 -1 1 -1 1 -1 1 -1


x = 1, 1 copies of 1
y = 3, 3 copies of -1

1, -1, -1, -1


How many ways can we split into subarrays that have the same sum


"""