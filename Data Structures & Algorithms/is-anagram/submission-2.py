class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmaps = defaultdict(int)
        hashmapt = defaultdict(int)
        for i in s:
            hashmaps[i] += 1

        
        for i in t:
            hashmapt[i] += 1

        return hashmaps == hashmapt
            
        