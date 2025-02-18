class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Solution using hash map - O(n) time and space complexity
        # majority_number = int(math.floor(len(nums)/2))
        # frequency_map = {}
        # for i in range(len(nums)):
        #     frequency_map[nums[i]] = frequency_map.get(nums[i], 0) + 1
        #     if frequency_map[nums[i]] > majority_number:
        #         return nums[i]
        
        # Boyer-Moore Voting Algorithm: O(n) time and constant space complexity
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

        