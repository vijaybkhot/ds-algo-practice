class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert = 0
        i = 0
        while i < len(nums):
            curr_num = nums[i]
            nums[insert] = curr_num
            insert += 1
            i += 1
            if i < len(nums) and nums[i] == curr_num:
                nums[insert] = curr_num
                insert += 1
                
            while i < len(nums) and nums[i] == curr_num:
                    i += 1
        
        return insert
                
                    
                    