class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = -math.inf

        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[r],heights[l]) * (r - l)
            ans = max(ans, area)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1


        return ans