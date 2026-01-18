
def run():
    input_str = input()
    count = 1
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            count = 1
        
        if count == 7:
            print("YES")
            return

    print("NO")

run()