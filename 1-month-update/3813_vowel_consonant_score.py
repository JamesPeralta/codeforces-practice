import math
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = 0
        c = 0
        for elem in s:
            if elem == " ":
                continue
            
            if elem in ['a', 'e', 'i', 'o', 'u']:
                vowels += 1
            elif elem.isdigit() is False:
                c+=1
        
        if c == 0:
            return 0
        return math.floor(vowels / c)