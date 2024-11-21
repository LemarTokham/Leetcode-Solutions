class Solution:
    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        # fill out both dicts 
        for c in s:
            d1[c] += 1
        for c in t:
            d2[c] += 1
        # key = letter, value = count of letter
        # checking the validity of both dictionaries
        if len(d1) != len(d2):
            return False
        for let, count in d1.items():
            if let in d1: # valid anagram should have same letter
                if count != d2[let]: # valid anagram should have the same count per letter
                    return False
            else:
                return False
        return True
