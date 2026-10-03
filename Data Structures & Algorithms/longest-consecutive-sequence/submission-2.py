class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        ans = 0   
        for i in nums:
            if i - 1 not in hashset:
                count = 1
                while (i + count) in hashset:
                    count += 1
                ans = max(ans, count)    

        return ans