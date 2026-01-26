import sys
input = sys.stdin.readline
tests = int(input())

# first = input()
for _ in range(tests):
    n = int(input())

    memo = [float("inf") for i in range(n)]
    unique = list(set([int(elem) for elem in input().split()]))
    unique.sort(reverse=True)
    for elem in unique:
        memo[elem - 1] = 1
    for i in range(n):
        # print("_____", i + 1)
        s = i
        if memo[i] == 1:
            # print(i + 1, 1)
            continue

        best = float("inf")
        # seen = False
        for elem in unique:
            x = (i + 1)
            # print(x, "//", elem, x % elem)
            if x % elem != 0:
                continue
            x= x // elem
            # print("HERE", x)
            if x < 1:
                continue
            best = min(best, memo[x - 1])
            break
        
        # print(i + 1, best)
        memo[s] = best + 1
    
    print(" ".join([str(elem) if elem != float("inf") else "-1" for elem in memo]))

"""
1
8
3 2 2 3 7 3 6 7

Array a
given n question

min number of elements to equal i.. Or report that it's impossible to achieve


"""