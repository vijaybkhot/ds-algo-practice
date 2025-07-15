class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        for n in range(1, len(nums)+1):
            num = num ^ n
        
        for n in nums:
            num = num ^ n
        
        return num