class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = []
        unique_nums = list(set(nums))
        unique_nums.sort()
        curr_sequence = 1
        for i in range(0, len(unique_nums)-1):
            if unique_nums[i+1] == unique_nums[i] + 1:
                curr_sequence += 1
            else:
                res.append(curr_sequence)
                curr_sequence = 1
        res.append(curr_sequence)
        return max(res)
