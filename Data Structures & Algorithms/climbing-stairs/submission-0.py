class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dfs(i):
            if i >= n: #we arrived at the top of the stairs
                return i == n
            if cache[i] != -1: #key in
                return cache[i]

            cache[i] = dfs(i + 1) + dfs(i + 2)  #the two options

            return cache[i]

        return dfs(0)