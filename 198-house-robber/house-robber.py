class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # # Bottom-up Dynamic programming approach
        # nums_record = [(0, 0)]*(n+1)    # with_curr, without_curr
        # nums_record[0] = (nums[0], 0)
        # nums_record[1] = (nums[1], nums_record[0][0])

        # for i in range(2, n):
        #     nums_record[i] = ((nums[i]+nums_record[i-1][1]), max(nums_record[i-1]))
        
        # return max(nums_record[n-1])

        # Space optimized DP
        max_num_1 = (nums[1], nums[0])
        for i in range(2, n):
            curr_max_set = ((nums[i]+ max_num_1[1]), max(max_num_1))
            max_num_1 = curr_max_set
        
        return max(max_num_1)

        