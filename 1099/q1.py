import sys
input = sys.stdin.readline
tests = int(input())

for _ in range(tests):
    first = ["2"] * int(input())
    _ = input()
    
    if len(first) == 1:
        print("1")
    else:
        print(" ".join(first))



"""
Given a permutation of size N

Find the min length of an array that contains the number p_i for each i


1


[1,2,3,4,5]

2, 1, 3

p_0 = 1

find the  min length of an array that contains the number 1?

[2, 1, 3, 4]

want to keep 4

"""