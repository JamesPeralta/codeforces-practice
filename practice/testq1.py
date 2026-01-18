nums = [2, 20,101]

largest = float("-inf")
for num in nums:
    if num % 2 == 0:
        largest = max(largest, num)

print(-1 if largest == float("-inf") else largest)
# return -1 if largest == float("-inf") else largest