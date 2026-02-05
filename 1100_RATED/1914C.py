tests = int(input())

for _ in range(tests):
    first = input().split()
    k = int(first[1])

    a_arr = [int(elem) for elem in input().split()]
    b_arr = [int(elem) for elem in input().split()]
    best = 0
    b_max = 0
    prefix_sum = 0
    for i in range(min(k, len(a_arr))):
        prefix_sum += a_arr[i]
        b_max = max(b_max, b_arr[i])
        remaining = k - (i + 1)
        # print(prefix_sum, remaining)
        best = max(best, prefix_sum + (remaining * b_max))
    print(best)