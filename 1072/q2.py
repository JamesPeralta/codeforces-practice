test_cases = int(input())

for i in range(test_cases):
    line = input().split()
    s = int(line[0])
    k = int(line[1])
    m = int(line[2])

    num_flips = m // k
    time_left = m % k
    is_odd = num_flips % 2 == 1

    if is_odd:
        time_left = min(k, s) - time_left
    else:
        time_left = s - time_left
    
    print(max(0, time_left))
