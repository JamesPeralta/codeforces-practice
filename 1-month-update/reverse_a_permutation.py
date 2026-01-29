# Pattern: Greedy — find longest sorted prefix of permutation (1,2,...,largest); then find index of max in remainder, reverse segment from end of prefix to that max to bring max into place
import sys
input = sys.stdin.readline
tests = int(input())

def reverse(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

# first = input()
for _ in range(tests):
    largest = int(input())
    arr = [int(elem) for elem in input().split()]

    start = 0
    index = 0
    while index < len(arr) and arr[index] == largest:
        largest -= 1
        index += 1

    if index < len(arr):
        best = arr.index(max(arr[index:]))
        reverse(arr, index, best)

    print(" ".join([str(elem) for elem in arr]))


"""

"""