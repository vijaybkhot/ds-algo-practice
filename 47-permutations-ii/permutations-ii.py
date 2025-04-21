class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # result = []
        # k = len(nums)

        # def dfs(start):
        #     if start == k:
        #         result.append(nums[:])
        #         return
        #     seen = set()
        #     for i in range(start, len(nums)):
        #         if nums[i] in seen:
        #             continue
        #         seen.add(nums[i])
        #         nums[start], nums[i] = nums[i], nums[start]     # Swap in place
        #         dfs(start+1)
        #         nums[start], nums[i] = nums[i], nums[start]     # Swap back - backtrack

        # nums.sort()
        # dfs(0)
        # return result

        res = []
        nums.sort()
        def dfs(start):
            if start == len(nums):
                res.append(nums[:])
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                nums[i], nums[start] = nums[start], nums[i]
                dfs(start+1)
                nums[i], nums[start] = nums[start], nums[i]
        
        dfs(0)
        return res
        