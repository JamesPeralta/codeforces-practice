# Pattern: Filter by constraint + greedy selection — keep towers within Manhattan radius, per quality keep lexicographically smallest (x,y), then return highest quality
import math
class Solution:
    def manhat(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        # best, best_dist = (float("-inf"),float("-inf")) , float("inf")

        can_pass = {}
        # curr_i = 0
        for a, b, q in towers:
            dist = self.manhat((a, b), center)
            if dist <= radius:
                if q in can_pass:
                    other = can_pass[q]
                    if a < other[0]:
                        can_pass[q] = (a, b)
                    elif a == other[0] and b < other[1]:
                        can_pass[q] = (a, b)
                else:
                    can_pass[q] = (a, b)

        new = [(elem, can_pass[elem])for elem in can_pass.keys()]
        new.sort(reverse=True)
        # print(new)
        if new:
            return list(new[0][1])
        return [-1, -1]