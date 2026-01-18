num_tests = int(input())


for i in range(num_tests):
    _ = input()
    words = input()

    # if i == 38:
    #     print("YEET", words)
    words= words.split()
    result = ""
    for word in words:
        option1 = word + result
        option2 = result + word
        if option1 <= option2:
            result = option1
        else:
            result = option2
    print(result)
