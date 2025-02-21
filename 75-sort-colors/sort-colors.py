class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # using insertion sort:
        for i in range(1, len(nums)):
            space = i
            curr_elem = nums[space]
            while space > 0 and nums[space-1] > curr_elem:
                nums[space] = nums[space-1]
                space = space - 1
            nums[space] = curr_elem
        return nums

        