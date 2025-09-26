class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        count = 0
        for i in range(len(nums)):
            side1 = nums[i]
            for j in range(i+1, len(nums)):
                side2 = nums[j]
                max_side3 = side1+side2
                k = bisect_right(nums, max_side3-1, lo=j+1)
                count += k - (j+1)
        
        return count


