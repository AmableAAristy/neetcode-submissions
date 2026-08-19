class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1
        
        ans = sorted(hashmap, key=hashmap.get, reverse=True)
        return ans[:k] 