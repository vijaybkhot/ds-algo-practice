class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for idx, num in enumerate(nums):
            curr_target = target - num
            if curr_target in nums_map:
                return [nums_map[curr_target] ,idx]
            nums_map[num] = idx
        