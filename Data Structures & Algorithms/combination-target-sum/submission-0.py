class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        nums.sort()


        def dfs(i, cur, total):
            #base case, if total == target... then we append the current array
            if total ==  target:
                ans.append(cur.copy())
                return
            
            for j in range(i, len(nums)):#since numbers can be repeated we can do this
                if total + nums[j] > target:
                    return #too much
                
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()

        dfs(0,[],0)

        return ans
            

