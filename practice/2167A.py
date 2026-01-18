# take the input.. input()
num_cases = input()
# print(num_cases)
for i in range(int(num_cases)):
    array = input().split(" ")
    side_length = array[0]

    hit_no = False
    for side in array[1:]:
        if side != side_length:
            hit_no = True
            break

    if hit_no == True:
        print("NO")
    else:
        print("YES")
