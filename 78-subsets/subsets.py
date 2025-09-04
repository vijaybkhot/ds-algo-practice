class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(i, curr_set):
            if i == len(nums):
                self.res.append(curr_set[::])
                return
            
            curr_set.append(nums[i])
            dfs(i+1, curr_set)
            curr_set.pop()
            dfs(i+1, curr_set)
        
        dfs(0, [])

        return self.res