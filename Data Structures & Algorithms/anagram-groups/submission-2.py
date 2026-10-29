class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            w = [0] * 26

            for c in word:
                w[ord(c) - ord('a')] += 1
            
            hashmap[tuple(w)].append(word)

        return list(hashmap.values())