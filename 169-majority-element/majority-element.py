class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_number = int(math.floor(len(nums)/2))
        
        frequency_map = {}
        for i in range(len(nums)):
            frequency_map[nums[i]] = frequency_map.get(nums[i], 0) + 1
            if frequency_map[nums[i]] > majority_number:
                return nums[i]
        

        