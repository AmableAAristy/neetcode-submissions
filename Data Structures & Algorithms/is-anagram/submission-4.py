class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False

        sList = [0] * 26
        tList = [0] * 26


        for c in s:
            sList[ord(c) - ord('a')] += 1
            
        for c in t:
            tList[ord(c) - ord('a')] += 1

        return tList == sList