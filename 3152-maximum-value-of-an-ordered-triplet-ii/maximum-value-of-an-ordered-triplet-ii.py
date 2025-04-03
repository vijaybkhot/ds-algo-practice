class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        left_max = [0] * n
        left_max[0] = nums[0]

        for i in range(1, len(nums)):
            left_max[i] = max(nums[i], left_max[i-1])
        
        right_max = [0] * n
        right_max[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i])
        
        max_triplet = float('-inf')
        for i in range(1, len(nums)-1):
            left_num = left_max[i-1]
            num = nums[i]
            right_num = right_max[i+1]
            max_triplet = max(max_triplet, (left_num - num) * right_num)
        
        return 0 if max_triplet < 0 else max_triplet

        