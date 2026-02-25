test = int(input())

def is_fair(num):
    tmp = num
    while num > 0:
        last = num % 10
        if last != 0 and tmp % last != 0:
            return False

        num = num // 10
        # print("b", num)

    return True

for _ in range(test):
    num = int(input())

    while True:
        # print("A")
        if is_fair(num) is False:
            num += 1
        else:
            break
    
    print(num)


"""
1
1234567890
       ^
1234568040

"""