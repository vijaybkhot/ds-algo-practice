class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_idx = 0
        max_num = max(nums)
        res = [0]*n

        for i in range(len(nums)):
            if nums[i] == max_num:
                res[i] = -1 
        for i in range(len(nums)):
            if res[i] == -1:
                continue
            j = i+1
            while j%n != i and nums[j%n] <= nums[i]:
                j += 1
            if i != j%n:
                res[i] = nums[j%n]

        return res
            
            