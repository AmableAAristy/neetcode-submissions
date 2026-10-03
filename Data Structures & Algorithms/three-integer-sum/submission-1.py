class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        ans = []

        for i , num in enumerate(nums):
            if i > 0 and nums[i - 1] == num:
                continue
            
            l = i + 1
            r = len(nums) - 1

            

            while l < r:
                target = num + nums[l] + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    ans.append([num,nums[l],nums[r]])
                    temp = nums[r]
                    while r > l and nums[r] == temp:
                        r -= 1 


        return ans
            