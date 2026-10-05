class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        ans = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            minHeight= min(heights[l], heights[r]) #w
            area = (r - l) * minHeight
            ans = max(ans, area)

            if minHeight == heights[l]:
                l += 1
            else:
                r -=1

        
        return ans