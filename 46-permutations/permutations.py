class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # k = len(nums)
        # result = []
        # def dfs(curr_path, remainder):
        #     if len(curr_path) == k:
        #         result.append(curr_path[:])
        #         return
        #     for i in range(len(remainder)):
        #         curr_path.append(remainder[i])
        #         new_remainder = remainder[:i]+remainder[i+1:] if len(remainder) > 1 else []
        #         dfs(curr_path, new_remainder)
        #         curr_path.pop()

        # dfs([], nums)
        # return result

        # Solution II: Swapping in place
        result = []
        k = len(nums)

        def dfs(start):
            if start == len(nums):
                result.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]     # Swap in place
                dfs(start+1)
                nums[start], nums[i] = nums[i], nums[start]     # Swap back - backtrack
        
        dfs(0)
        return result

