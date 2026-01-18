"""

"""
test_cases = int(input())

for _ in range(test_cases):
    first = input()
    arr = input()
    n, k = first.split(" ")
    n = int(n)
    k = int(k)
    arr = [int(elem) for elem in arr.split()]
    if k > 1:
        print("yes")
    else:
        is_sorted = True
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                is_sorted = False
        
        if is_sorted:
            print("YES")
        else:
            print("NO")
