class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_operations = 0
        # while True:
        #     nums_set = set(nums)
        #     if len(nums_set) == len(nums):
        #         return num_operations
            
        #     bitwise_and = 1

        if len(set(nums)) == 1:
            return 0
        return 1