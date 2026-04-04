import sys
input = sys.stdin.readline
tests = int(input())
# https://codeforces.com/problemset/problem/1878/C
for _ in range(tests):
    first = input().split()
    n, k, x = int(first[0]), int(first[1]), int(first[2])

    lowest = (k*(k+1))/2
    highest = (n*(n+1))/2 - ((n-k)*((n-k)+1))/2
    if x < lowest or x > highest:
        print("NO")
    else:
        print("YES")
# target > k(k + 1)/ 2
#  return False
# else:

"""
Choose k distinct integers so that they add up to x

n = choose between 1 to n
k = number of distinct integers
x = target


1,2,3,4,5,6,7,8,9,10

target = 10
1 = 10
2 = 8, 2
3 = 7,2,1
4 = 1,2,3,4

target > k(k + 1)/ 2
 return False
else:
return True

target > first k in seq then false..

otherwise return true

14 1
13 2 1


can we hit any target


5 = 1,2,3,4,5


n = 10
k = 3

lowest = 6? Is it in the range of lowest and highest?
highest = 27?
target = 1
"""