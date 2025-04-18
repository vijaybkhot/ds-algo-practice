class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.xor = 0
        
        def dfs(index, total):
            if index == len(nums):
                return total
            
            include = dfs(index+1, total^nums[index])
            exclude = dfs(index+1, total)

            return include + exclude
        
        return dfs(0, 0)

