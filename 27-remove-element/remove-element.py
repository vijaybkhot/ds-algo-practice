class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        right_pointer = len(nums)-1
        left_pointer = 0
        output = 0

        while left_pointer <= right_pointer:
            if nums[left_pointer]==val:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                right_pointer -= 1
            else:
                left_pointer += 1
        
        return left_pointer
        
                    
        


        