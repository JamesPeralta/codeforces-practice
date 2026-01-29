# Pattern: Hashing / normalization — normalize each word to a canonical form (e.g. shift so first char is 'a'), then count pairs with same normalized form (Caesar-equivalent)
from collections import defaultdict

class Solution:
    def normalize(self, word):
        dist_from_a = abs(ord('a') - ord(word[0]))
        new_dist = []
        for char in word:
            if ord(char) - dist_from_a < 97:
                from_zero = abs(ord('a') - ord(char))
                new_dist.append(123 - (dist_from_a - from_zero))
            else:
                # dist_to_a
                new_dist.append(ord(char) - dist_from_a)

        # print(new_dist)
        return new_dist
        
    def countPairs(self, words: List[str]) -> int:
        seen = defaultdict(int)
        result = 0
        for word in words:
            normed = tuple(self.normalize(word))
            if normed in seen:
                result += seen[normed]
            seen[normed] += 1
        # print(self.normalize("fusion"))
        # print(self.normalize("layout"))
        return result
"""

fusion
6

anchor everything to a..


"""