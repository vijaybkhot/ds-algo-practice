class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums_set = set()
        res = 0
        for num in nums:
            if num not in nums_set and num > 0:
                nums_set.add(num)
                res += num
        if res == 0:
            return max(nums)
        
        return res
        