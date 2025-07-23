class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        num_op = 0
        l, r = 0, len(nums)-1

        while l < r:
            curr_sum = nums[l]+nums[r]
            if curr_sum == k:
                l += 1
                r -= 1
                num_op += 1
            elif curr_sum < k:
                l += 1
            else:
                r -= 1
        
        return num_op