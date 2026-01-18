import math
tests = int(input())

for _ in range(tests):
    first = int(input())
    roots = []
    for i in range(first):
        roots.append(str(i + 1))
    print(" ".join(roots))
    


# 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2056
# 5012, 10024

"""
Debrief

- Could have just output any number..
- Any integer is the square root of some number

Need to study the relationship between sqrt and power..
"""
