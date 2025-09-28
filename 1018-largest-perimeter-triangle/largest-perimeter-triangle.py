class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0

        # for k in range(n-1, 1, -1):  # largest side
        #     for j in range(k-1, 0, -1):
        #         for i in range(j-1, -1, -1):
        #             if nums[i]+nums[j] > nums[k]:
        #                 return nums[i]+nums[j]+nums[k]

        for k in range(n-1, 1, -1):
            if nums[k-2] + nums[k-1] > nums[k]:
                return nums[k-2] + nums[k-1] + nums[k]
                
        return 0

