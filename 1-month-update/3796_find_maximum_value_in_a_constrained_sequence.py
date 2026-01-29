class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        all_rest = [float("inf") for i in range(n)]
        for k, v in restrictions:
            all_rest[k] = v
        for i in range(n - 2, -1, -1):
            if all_rest[i + 1] == float("inf"):
                continue
            # print(i)
            all_rest[i] = min(all_rest[i], all_rest[i + 1] + diff[i])
        # print(all_rest)
        result = 0
        curr = 0
        # print("_seq__")
        # print(0)
        for index, num in enumerate(diff):
            curr += num
            curr = min(all_rest[index + 1], curr)
            result = max(result, curr)
            # print(curr)
        return result


"""
Input:
n = 10
restrictions = [
    [3,1],
    [8,1]]
diff = [2,2,3,1,4,5,1,1,2]

0,

maxval caps.. Can we get to maxval for an index or closer?

Increase it as high as we can then bring it back down based on maxVal

always going to be increasomg
"""