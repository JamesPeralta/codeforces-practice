# print("HELLO WORLD")
"""
- n candidate players
- ith player has a power of P
- zero or more teams from the n candidates
- each player may join at most one team
- will face one enememy team with a power of D.
- In each match it will defeat the team if the sum of powers from the formed
players is strictly greater than D.
- can change the power of each player to be the biggest player power on the tea

50, 60, 70, 80, 90, 100
                     ^
^

- intutition. We match the large ones with the small ones because they
  will increase the result the most.  Two pointers. One on each side.

"""
# tests = int(input())

# for _ in range(tests):
first = input().split()
D = int(first[1])
nums = [int(elem) for elem in input().split()]
nums.sort()

left, right = 0, len(nums) - 1
result = 0
while right >= 0 and nums[right] > D:
    result += 1
    right -= 1

while left < right:
    curr = nums[right]
    while left < right and curr <= D:
        curr += nums[right]
        left += 1
        # print("HERE")

    if curr > D:
        result += 1

    right -= 1
print(result)
"""
50,x,x
   l
     r
"""