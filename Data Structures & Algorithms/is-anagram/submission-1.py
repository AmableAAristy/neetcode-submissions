class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        w1 = [0] * 26
        w2 = [0] * 26

        for c in s:
            w1[ord(c) - ord('a')] += 1
        
        for c in t:
            w2[ord(c) - ord('a')] += 1

        return w1 == w2