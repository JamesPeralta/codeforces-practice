test_cases = int(input())

for i in range(test_cases):
    num_students = input()
    student_skills = input()

    n, x = num_students.split(" ")
    student_skills = sorted(map(lambda x: int(x), student_skills.split(" ")), reverse=True)
    max_groups = 0
    smallest, size = float("inf"), 0
    for skill in student_skills:
        smallest = min(smallest, skill)
        size += 1
        if smallest * size >= int(x):
            max_groups += 1
            smallest = float("inf")
            size = 0

    print(max_groups)


"""
10:28 PM
@sebastianponce4462
​​you are sorting strings, not ints


10:28 PM
@sebastianponce4462
​​so it sorts alphabetically so 91 is after 10000

1
"""