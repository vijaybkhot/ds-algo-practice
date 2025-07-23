class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n
        res = [0]*n

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1]*nums[i]
        
        res[0], res[-1] = suffix[1], prefix[n-2]
        for i in range(1, n-1):
            res[i] = prefix[i-1]*suffix[i+1]
        return res