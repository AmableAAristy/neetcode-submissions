class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        i = 0
        j = 1

        while j < len(prices):
            temp = prices[j] - prices[i]
            ans = max(temp, ans)

            if prices[i] > prices[j]:
                i = j
            j += 1 

        return ans