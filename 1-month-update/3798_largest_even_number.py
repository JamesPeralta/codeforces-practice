# Pattern: Greedy — remove trailing '1's from the right so the string ends with '2' (largest even digit in binary string)
class Solution:
    def largestEven(self, s: str) -> str:
        s_arr = [elem for elem in s]
        while len(s_arr) and s_arr[-1] == "1":
            s_arr.pop()
        return "".join(s_arr)
        # if s[-1] == "1":
        #     if len(s) == 1 or s[-2] == "1":
        #         return ""
        #     else:
        #         return s[:-1]
        # else:
        #     return s
        
        # else:
        #     index_of_one = s.find("1")
        #     if index_of_one != -1:
        #         remove_one = []
        #         for i in range(len(s)):
        #             if i == index_of_one:
        #                 continue
        #             remove_one.append(s[i])
        #         return "".join(remove_one)
            
        #     index_of_two = s.find("2")                    
        #     remove_two = []
        #     for i in range(len(s)):
        #         if i == index_of_two:
        #             continue

        #     return "".join(remove_two)

"""
Has to end with 2


12222

delete the first 1 going from left to right

delete the first 2
"""