class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # # This solution was developed independently by me without external help.
        # # edge cases
        # if not nums:
        #     return 0
        # if len(nums)== 1:
        #     if nums[0] % k != 0:
        #         return 0
        #     else:
        #         return 1
        
        # res = 0
        # # Remainder frequency hash map
        # remainder = {}
        # prefix = 0
        # for index, num in enumerate(nums, start=0):
        #     prefix += num
        #     curr_remainder = prefix % k
        #     remainder.setdefault(curr_remainder, []).append(index)
        #     res += len(remainder[curr_remainder]) - 1 if curr_remainder !=0 else len(remainder[curr_remainder])
                    
        # return res
        
        # More optimal solution

        res = 0
        remainder_count = {0: 1}  # To count the number of times a remainder has appeared
        prefix = 0
        for num in nums:
            prefix += num
            curr_remainder = prefix % k
            if curr_remainder < 0:
                curr_remainder += k
            # If the remainder has appeared before, it means there are `remainder_count[curr_remainder]` subarrays ending here that are divisible by k
            res += remainder_count.get(curr_remainder, 0)
            
            # Update the count of this remainder
            remainder_count[curr_remainder] = remainder_count.get(curr_remainder, 0) + 1
        
        return res


