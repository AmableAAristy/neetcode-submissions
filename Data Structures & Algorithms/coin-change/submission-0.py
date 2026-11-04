class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(target):
            if target < 0:
                return math.inf

            if target == 0:
                return 0
            if target in memo:
                return memo[target]

            best = math.inf

            for c in range(len(coins)):
                choice1 = 1 + dfs(target - coins[c])
                best = min(choice1, best)
            memo[target] = best

            return memo[target]

        ans = dfs(amount)

        return -1 if math.inf == ans else ans