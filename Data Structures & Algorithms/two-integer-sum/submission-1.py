class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = defaultdict(int)

        for n in range(len(nums)):
            if nums[n] in hashmap:
                return [hashmap[nums[n]], n]
            
            hashmap[target - nums[n]] = n
        
        return []