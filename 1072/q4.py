test_cases = int(input())

for i in range(test_cases):
    line = input().split()
    n, k = int(line[0]), int(line[1])
    left, right = 0, n
    while left < right:
        mid = left + (right - left) // 2

        turns_it_takes = (mid // 2) + 1
        print(mid, turns_it_takes)
        if turns_it_takes > k:
            right = mid
        else:
            left = mid + 1
    
    print(left)
