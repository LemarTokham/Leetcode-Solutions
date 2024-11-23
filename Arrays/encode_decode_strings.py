class Solution:
    from collections import defaultdict
    def encode(self, strs: List[str]) -> str:
        words = ""
        for s in strs:
            words += str(len(s)) + '#' + s
        return words
        
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # stores the length of the coming string
            i = j + 1
            j = length + i
            res.append(s[i:j])
            i = j
        return res