# Pattern: Brute force enumeration + rotation check — try all 4-combinations of words, for each try 4 rotations and validate square constraints (top-left=left-top, etc.)
class Solution:
    def check_square(self, top, right, bot, left):
        # print(top, right, bot, left)
        if top[0] != left[0]:
            return False
        if top[3] != right[0]:
            return False
        if bot[0] != left[3]:
            return False
        if bot[3] != right[3]:
            return False

        return True

    def rotate(self, top, right, bot, left, result):
        elems = [top, right, bot, left]
        for i in range(4):
            if self.check_square(elems[0],elems[1],elems[2],elems[3]):
                result.append((elems[0],elems[3], elems[1],elems[2]))

            last_elem = elems.pop()
            
            elems.insert(0, last_elem)

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        result = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                for k in range(j + 1, len(words)):
                    for l in range(k + 1, len(words)):
                        i_elem = words[i]
                        j_elem = words[j]
                        k_elem = words[k]
                        l_elem = words[l]
                        
                        # Permutations
                        self.rotate(i_elem, j_elem, k_elem, l_elem, result)
                        self.rotate(i_elem, j_elem, l_elem, k_elem, result)
                        self.rotate(i_elem, k_elem, j_elem, l_elem, result)
                        self.rotate(i_elem, k_elem, l_elem, j_elem, result)
                        self.rotate(i_elem, l_elem, j_elem, k_elem, result)
                        self.rotate(i_elem, l_elem, k_elem, j_elem, result)
        result = sorted(result)
        return result
