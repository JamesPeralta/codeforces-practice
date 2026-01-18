"""
how does increasing a number affect the result


1, 4, 10 -> 3
1, 4, 10 -> 80

1,5,10 -> 50

40

Closeset to 2, 3, 4, or 5
5*(any terms)

distance from 

​​you can get the closest multiple of k to the n with the formula , n + (k - n%k)

What's the closest to being divisible by k?

loop over each element and % by k

then for each element abs(k - m)?

6 % 5 = 1
9
k = 5, 5 - 4 = 1 distance 

10
"""

test_cases = int(input())

def test():
    first = input()
    n, k = first.split(" ")
    n = int(n)
    k = int(k)


    second = input()
    nums = [int(elem) % k for elem in second.split(" ")]
    closest = float("inf")
    num_1s = 0

    for num in nums:
        if num == 0:
            closest = 0
        else:
            closest = min(closest, k - num)
    # ​if u have two odds , answer is 2, if u have two even , 
    # answer is 0, if u have one even one odd, answer is 1, otherwise the answer is distance

    # 2k 2( j + 1) -> 4

       # if k == 4:
    k_4_min = float("inf")
    num_odds = 0
    num_evens = 0
    for num in nums:
        if num % 4 == 0:
            k_4_min = 0
            num_evens += 1
        if num % 2 == 0:
            num_evens += 1
        else:
            num_odds += 1
    
    if num_evens >= 2 or k_4_min == 0:
        k_4_min = 0
    elif num_evens >= 1 and num_odds >= 1:
        k_4_min = 1
    elif num_odds >= 2:
        k_4_min = 2
    else:
        k_4_min = 3

    if k == 4:
        print(min(k_4_min, closest))
    else:
        print(closest)


for _ in range(test_cases):
    test()

"""
2
2
1
0
2
0
1
2
0
1
1
4
0
4
3
"""