class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = nums[0]

        for next_num in nums[1:]:
            num = num^next_num
        
        return num

        