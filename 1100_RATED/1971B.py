print("HELLO WORLD")
import math

print(math.comb(2, 1))

class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        res = 0
        msb = k
        while math.comb(msb, k) < n:
            msb += 1
        for cur in range(msb - 1, -1, -1):
            combs_if_0 = math.comb(cur, k)
            if n <= combs_if_0:
                continue
            else:
                res += 2 ** cur
                n -= combs_if_0
                k -= 1
                if k == 0:
                    break
        return res