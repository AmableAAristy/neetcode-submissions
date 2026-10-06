class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenNums = len(nums)
        prefix = [1] * lenNums
        postfix = [1] * lenNums
        ans = [1] * lenNums


        for i in range(1, lenNums):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(lenNums - 2, -1, -1 ):
            postfix[i] = nums[i + 1] * postfix[i + 1]

        for i in range(0, lenNums):
            ans[i] = prefix[i] * postfix[i]


        return ans