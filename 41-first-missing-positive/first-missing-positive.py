class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Brute force solution:
        # max_num = max(nums)
        # for num in range(1, max_num):
        #     if num not in nums:
        #         return num
        
        # return max_num + 1

        # # 2nd Brute force solution
        # range_num = len(nums)
        # for i in range(1, range_num+2):
        #     if i not in nums:
        #         return i
        # return range_num + 2

        # Using hash set
        nums_set = set(nums)
        for i in range(1, len(nums_set)+1):
            if i not in nums_set:
                return i
        
        return len(nums_set) + 1


                

        