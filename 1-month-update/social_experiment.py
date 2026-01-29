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