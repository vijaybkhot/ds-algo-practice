class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # # Brute force solution:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # More optimal solution:
        complement_index_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in complement_index_map:
                return [complement_index_map[nums[i]] , i]
            else:
                complement_index_map[complement] = i
        