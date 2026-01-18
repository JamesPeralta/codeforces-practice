"""

"""
test_cases = int(input())

for _ in range(test_cases):
    input_str = input()
    num_0s = 0
    num_1s = 0

    for elem in input_str:
        if elem == "0":
            num_0s += 1
        else:
            num_1s += 1
    
    index = 0
    while index < len(input_str):
        if input_str[index] == "0":
            if num_1s == 0:
                break
            num_1s -= 1
        else:
            if num_0s == 0:
                break
            num_0s -= 1

        index += 1
    # print(index)
    print(len(input_str) - index)
