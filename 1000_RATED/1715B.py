# print("YO")
"""

- B = Divide each element by a K and Sum the result
- sum = s and beauty is b

n = num of elems
k = divide each by
b = beauty is equal to b
s = sum of elements of res

3 6 3 19
n k b s

We need to equal s and be of n.

Maybe just keep all of s in one and then n

10


"""


"""
If s / k < b we're done
If s / k == b we're done alse

if s / k > b. We can try shrinking s by spreading it across
more cells. We can pretty much just shrink it by only  n - 1
"""

tests = int(input())


for _ in range(tests):
    first = input().split()
    n = int(first[0])
    k = int(first[1])
    b = int(first[2])
    s = int(first[3])
    fill = 0

    res = [s]
    while (res[0] // k) > b and len(res) < n:
        res[0] -= (k-1)
        res.append(k-1)

    if res[0] // k == b:
        while len(res) < n:
            res.append(0)
        
        print(" ".join([str(elem) for elem in res]))
    else:
        print("-1")
