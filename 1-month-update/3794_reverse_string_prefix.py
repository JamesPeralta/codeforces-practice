class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        first_k = "".join(reversed(s[:k]))
        return first_k + s[k:]