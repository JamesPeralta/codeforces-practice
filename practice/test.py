"""
Q1: Write me code that loops over an array from left to right 3 times. Prints out it's path.
Clock wise.
"""

test_array = [1, 2, 3, 4, 5, 6]

def q1(nums):
    for i in range(len(test_array) * 3, 0, -1):
        print(test_array[(i - 1) % len(test_array)])


q1(test_array)

"""
Q2: Write me code that loops over an array from right to left 3 times. Prints out it's path.
counter clock wise.
"""

def q2(nums):
    pass