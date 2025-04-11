class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(index, output):
            if index == len(nums):
                result.append(output)
                return
            include_subset = output + [nums[index]]
            exclude_subset = output
            dfs(index + 1, include_subset)
            dfs(index + 1, exclude_subset)

        result = []
        dfs(0, [])
        return result
        