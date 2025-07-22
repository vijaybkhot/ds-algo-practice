class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert = 1
        prev = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == prev:
                continue
            else:
                nums[insert] = nums[i]
                insert += 1
                prev = nums[i]
                
        return insert
            

