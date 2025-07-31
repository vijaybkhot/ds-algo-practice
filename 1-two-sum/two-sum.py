class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_map = dict()

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in complement_map:
                return [idx, complement_map[complement]]
            else:
                complement_map[num] = idx