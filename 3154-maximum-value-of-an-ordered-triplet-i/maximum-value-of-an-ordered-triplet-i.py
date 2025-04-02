class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        # max_left_value = max(nums[:-2])
        # max_left_index = nums[:-2].index(max_left_value)
        # min_mid_value = min(nums[max_left_index+1:-1])
        # min_left_index = nums[max_left_index+1:-1].index(min_mid_value)
        
        # max_right_value = max(nums[min_left_index+1:])

        # res = (max_left_value - min_mid_value) * max_right_value

        # return res if res > 0 else 0
        # max_left_value = []
        # for i in range(0, len(nums)-2):
        #     max_left_value.append(max(nums[i:-2]))

        # min_mid_value = []
        # for i in range(1, len(nums)-1):
        #     min_mid_value.append(min(nums[i:-1]))

        # max_right_value = []
        # for i in range(2, len(nums)):
        #     max_right_value.append(max(nums[i:]))

        # res = (max_left_value[0] - min_mid_value[0]) * max_right_value[0]
        # for i in range(1, len(max_left_value)):
        #     res = max(res, (max_left_value[i] - min_mid_value[i]) * max_right_value[i])
        
        # return res if res > 0 else 0
        n = len(nums)
        res = 0

        # Precompute left_max[i] (Max value from nums[0] to nums[i-1])
        left_max = [0] * n
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])

        # Precompute right_max[i] (Max value from nums[i+1] to nums[n-1])
        right_max = [0] * n
        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        # Iterate over the middle element
        for j in range(1, n - 1):
            if left_max[j - 1] > nums[j] and right_max[j + 1]:
                res = max(res, (left_max[j - 1] - nums[j]) * right_max[j + 1])

        return res


                
                

                
                

