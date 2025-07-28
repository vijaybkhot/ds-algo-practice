class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOrValue = 0

        for num in nums:
            maxOrValue = maxOrValue | num
        
        dp = {}
        def dfs(i, currOr):
            if (i, currOr) in dp:
                return dp[(i, currOr)]
            if i == len(nums):
                if currOr == maxOrValue:
                    return 1
                else:
                    return 0
            
            total_subs = 0

            total_subs += dfs(i+1, currOr | nums[i])
            total_subs += dfs(i+1, currOr)

            dp[(i, currOr)] = total_subs
            return total_subs
        
        return dfs(0, 0)
