class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break

            mid = (l + r) // 2

            if nums[mid] >= nums[l]: #it pivots before mid 
                l = mid + 1

            else: 
                r = mid - 1


                
            minimum = min(minimum, nums[mid])

        return minimum
