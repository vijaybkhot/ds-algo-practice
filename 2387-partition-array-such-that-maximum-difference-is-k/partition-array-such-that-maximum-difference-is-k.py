class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        start = nums[0]
        i = 0
        while i < len(nums):
            if nums[i] > start + k:
                count += 1
                start = nums[i]
            i += 1
        return count



        