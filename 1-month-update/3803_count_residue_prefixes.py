class Solution:
    def residuePrefixes(self, s: str) -> int:
        chars = set()
        res = 0
        for i, chara in enumerate(s):
            chars.add(chara)
            if len(chars) == (i + 1) %3:
                res += 1

        return res