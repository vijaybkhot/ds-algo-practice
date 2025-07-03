class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start):
            if start == len(nums):
                res.append(nums[::])
                return
            
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                dfs(start+1)
                nums[i], nums[start] = nums[start], nums[i]
        
        dfs(0)
        return res








        
        # # Solution using slicing - O(n*n!) time - extra n for creating slices. O(n^2) space - extra n for creating sliced lists along with n for recursion stack
        # # k = len(nums)
        # # result = []
        # # def dfs(curr_path, remainder):
        # #     if len(curr_path) == k:
        # #         result.append(curr_path[:])
        # #         return
        # #     for i in range(len(remainder)):
        # #         curr_path.append(remainder[i])
        # #         new_remainder = remainder[:i]+remainder[i+1:] if len(remainder) > 1 else []
        # #         dfs(curr_path, new_remainder)
        # #         curr_path.pop()

        # # dfs([], nums)
        # # return result

        # # # Solution II: Swapping in place - More optimal - O(n!) time and O(n) space for recursion tree
        # # result = []
        # # k = len(nums)

        # # def dfs(start):
        # #     if start == len(nums):
        # #         result.append(nums[:])
        # #         return
            
        # #     for i in range(start, len(nums)):
        # #         nums[start], nums[i] = nums[i], nums[start]     # Swap in place
        # #         dfs(start+1)
        # #         nums[start], nums[i] = nums[i], nums[start]     # Swap back - backtrack
        
        # # dfs(0)
        # # return result

        # # res = []
        # # def dfs(path, rem):
        # #     if len(nums) == len(path):
        # #         res.append(path[:])
            
        # #     for i in range(len(rem)):
        # #         path.append(rem[i])
        # #         new_rem = rem[:i] + rem[i+1:]
        # #         dfs(path, new_rem)
        # #         path.pop()
                
        # # dfs([], nums[:])
        # # return res

        # res = []

        # def dfs(start):
        #     if start == len(nums):
        #         res.append(nums.copy())
        #         return

        #     for i in range(start, len(nums)):
        #         nums[i], nums[start] = nums[start], nums[i]
        #         dfs(start+1)
        #         nums[start], nums[i] = nums[i], nums[start]
        
        # dfs(0)
        # return res

                

        