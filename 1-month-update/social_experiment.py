# Pattern: Parity / modulo — if n <= 3 answer is n; else answer is n % 2 (remainder when splitting people into groups of 3)
test_cases = int(input())

for i in range(test_cases):
    num_people = int(input())
    if num_people <= 3:
        print(num_people)
    else:
        remainder = num_people % 2
        print(remainder)

"""
Split by 3
"""