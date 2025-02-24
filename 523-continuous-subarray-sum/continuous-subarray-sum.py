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
        prefix = nums[0]
        for i in range(len(nums)):
            curr_remainder = prefix % k
            if curr_remainder in hash_map and i - hash_map[curr_remainder] >= 2:
                return True
            if curr_remainder not in hash_map:
                hash_map[curr_remainder] = i
            prefix = prefix + (nums[i+1] if i + 1 < len(nums) else 0)

        return False
