# Pattern: Combinatorics / digit DP — build nth smallest number with k one-bits by placing bits from high to low using binomial coefficients (C(bit_position, remaining_bits)) to skip ranges
import math
class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        bits = []
        for i in range(k):
            bits.append(k - i - 1)

        # [2, 1]
        #  
        curr_num = 1
        for i in range(len(bits)):
            combs, last_combs = 1, 1
            while combs < n:
                bits[i] += 1
                curr = math.comb(bits[i], len(bits) - (i + 1))
                last_combs = combs
                combs += curr
            n -= last_combs

        result = [str(0) for _ in range(50)]
        for elem in bits:
            result[elem] = str(1)
        result.reverse()

        return int("".join(result), 2)

"""
n = give me the nth number in a sequence
k = number of bits



"""



















