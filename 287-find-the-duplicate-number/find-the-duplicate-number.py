class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # Using hash set - not constant extra space
        # nums_set = set()
        # for num in nums:
        #     if num in nums_set:
        #         return num
        #     nums_set.add(num)

        # Negative Marking
        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx] < 0:
                return abs(idx)
            nums[idx] *= -1

        


        