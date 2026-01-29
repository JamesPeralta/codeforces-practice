# Pattern: Ad-hoc / direct output — output roots as "1 2 3 ... n" for given n (problem-specific)
import math
tests = int(input())

power_of_two = [1, 2, 4, 8, 16, 32, 64, 128,
256, 512, 1024, 2048, 4096, 8192, 16384, 32768,
 65536, 131072, 262144, 524288]
curr = 1
for _ in range(1, 21):
    power_of_two.append(curr)
    curr *= 2

# print(power_of_two)
for _ in range(tests):
    first = int(input())
    roots = []
    for i in range(first):
        roots.append(str(i + 1))
    print(" ".join(roots))
    


# 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2056
# 5012, 10024