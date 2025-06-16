class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump, i = 0, 0
        while i < len(nums):

            max_jump = max(max_jump, nums[i]+i)

            if max_jump >= len(nums)-1:
                return True

            elif i+1 <= max_jump:
                i += 1

            else:
                return False

        return True
        