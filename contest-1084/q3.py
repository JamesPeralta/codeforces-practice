import sys
input = sys.stdin.readline
tests = int(input())


for _ in range(tests):
    _ = int(input())
    nums = input().strip()
    stack = []
    for num in nums:
        if stack and num == stack[-1]:
            stack.pop()
        else:
            stack.append(num)
    
    if stack:
        print("NO")
    else:
        print("YES")

"""
1
6
llmllm
"""