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
        #Create a prefix sum array
        prefix = [0]
        for i in range(len(nums)):
            if i > 0 and nums[i] == 0 and nums[i-1] == 0:
                return True
            prefix.append(prefix[-1] + nums[i])
        
            
        # Creating a hash map to store remainders
        hash_map = {0:-1}
        for i in range(1, len(prefix)):
            curr_remainder = prefix[i] % k
            if curr_remainder in hash_map and i > 1 and i - hash_map[curr_remainder] >= 2:
                return True
            if curr_remainder not in hash_map:
                hash_map[curr_remainder] = i
        
        return False