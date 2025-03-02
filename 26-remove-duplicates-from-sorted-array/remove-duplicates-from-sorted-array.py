class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        n = len(nums)
        insert_pos = 1
        element_finder = insert_pos
        while element_finder < n and insert_pos < n:
            if nums[element_finder] == nums[insert_pos-1]:
                element_finder += 1
            else:
                nums[insert_pos] = nums[element_finder]
                insert_pos += 1
                element_finder += 1
        return insert_pos
        

        