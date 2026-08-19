class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)


        for w in strs:
            word = [0] * 26

            for c in w:
                word[ord(c) - ord('a')] += 1
            
            ans[tuple(word)].append(w)

        return list(ans.values())
        
        
            

            