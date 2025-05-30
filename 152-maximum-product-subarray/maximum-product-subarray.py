class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # # Dynamic programming approach - Bottom up
        # res = nums[0]
        # max_product = [(0, 0)]*len(nums)
        # max_product[0] = (nums[0], nums[0])
        # for i in range(1, len(nums)):
        #     max_num = max(nums[i], nums[i]*max_product[i-1][0], nums[i]*max_product[i-1][1])
        #     min_num = min(nums[i], nums[i]*max_product[i-1][1], nums[i]*max_product[i-1][0])
        #     max_product[i] = (max_num, min_num)
        #     res = max(res, max_num)
        
        # return res

        # Space optimized Dynamic programming approach - Bottom up
        res = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        for i in range(1, len(nums)):
            max_num = max(nums[i], nums[i]*curr_max, nums[i]*curr_min)
            min_num = min(nums[i], nums[i]*curr_max, nums[i]*curr_min)
            curr_max = max_num
            curr_min = min_num
            res = max(res, max_num)
        
        return res
