class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}


        def dfs(i):
            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]


            #choice 1 1 floor
            hop1 = cost[i] + dfs(i + 1)
            #choice 2 2 floors
            hop2 = cost[i] + dfs(i + 2)

            memo[i] = min(hop1, hop2)

            return memo[i]

        return min(dfs(0), dfs(1))