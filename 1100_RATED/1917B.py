tests = int(input())

for _ in range(tests):
    _ = input()
    input_str = input()
    seen = set()
    result = 0
    for i, elem in enumerate(input_str):
        if elem not in seen:
            seen.add(elem)
            result += (len(input_str) - i)
    print(result)
