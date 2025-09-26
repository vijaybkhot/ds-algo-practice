class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        # nums.sort()
        # count = 0
        # for i in range(len(nums)):
        #     side1 = nums[i]
        #     for j in range(i+1, len(nums)):
        #         side2 = nums[j]
        #         max_side3 = side1+side2
        #         k = bisect_right(nums, max_side3-1, lo=j+1)
        #         count += k - (j+1)
        
        # return count

        nums.sort()
        n = len(nums)
        count = 0
        
        for k in range(n-1, 1, -1):  # largest side
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count

