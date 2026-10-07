class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        ans = 0

        i = 0
        j = 1

        while j < len(nums):
            ans = max(ans, nums[j] - nums[i])

            if nums[i] > nums[j]:
                i = j
            j += 1 

        return ans