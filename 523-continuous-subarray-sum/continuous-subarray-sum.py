class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Edge cases
        if len(nums) < 2:
            return False
            
        # Creating a hash map to store remainders
        hash_map = {0: -1}
        prefix = 0
        for i in range(len(nums)):
            prefix = prefix + nums[i]
            curr_remainder = prefix % k
            if curr_remainder not in hash_map:
                hash_map[curr_remainder] = i
            elif i - hash_map[curr_remainder] >= 2:
                return True 

        return False
