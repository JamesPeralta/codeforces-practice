"""
0001
0010
0011
0100
0101
0110
0111
1000

0102034
0101011
AABBAAA
 l   r

010

Two functions:
- Update
- Query
 
nums = [1,3,5,2,5]
pfx = [1,4,9,11,16]

nums = [1,3,10,2,5]
pfx = [1,4,14,16,21]


0102034
AABBAAA



"""

total = [0] * for i in 

class BinaryIndexedTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
        self.n = n

    def lsb(self, i):
        return i & -i

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += self.lsb(i)
    
    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= self.lsb(i)
        return total
#       1  2  3  4  5 
nums = [1, 3, 5, 2, 5]
bit = BinaryIndexedTree(len(nums))
for i in range(1, len(nums) + 1):
    bit.update(i, nums[i-1])

# Goes to 10
# new number - old
# 
bit.update(3, 10)

# pfx = [1,4,9,11,16]
assert bit.query(1) == 1
assert bit.query(2) == 4
assert bit.query(3) == 19
assert bit.query(5) == 26
print("PASSED")