"""
odd + odd = even
even + even = even
odd + even = odd

even,

each color has at least one element colored

choose one element -> even

See if we add up the rest is it even

pick an odd -> some others and see if it's odd

4
4 3 4 5

4 12

evens = 2
odds = 2

even +odd, even + odd

even, odd

even, odd = odd
odd = odd

5
5 4 3 2 1

odds = 3
evens = 2 -> even

2 odds = even

We just need to split the .. if odds % 2 != 1

1, 1
"""
test_cases = int(input())

for _ in range(test_cases):
    _ = input()
    arr = input()
    elems = [int(elem) for elem in arr.split(" ")]
    num_odds = 0
    for elem in elems:
        if elem % 2 == 1:
            num_odds += 1
    
    if num_odds % 2 == 1:
        print("No")
    else:
        print("YES")

