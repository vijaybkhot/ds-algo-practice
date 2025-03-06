class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # # Brute force solution
        # for i in range(len(nums)):
        #     j = i + 1
        #     while j < len(nums) and j <= i + k:
        #         if nums[i] == nums[j]:
        #             return True
        #         j += 1
        
        # return False
        # Using sliding window and a hash set to track duplicates in a sliding window sub array
        unique_set = set()
        # initiate a sliding window and add the elements to the hashset
        for i in range(0, k+1):
            if i < len(nums):
                if nums[i] in unique_set:
                    return True
                unique_set.add(nums[i])
        
        # Slide widow and check each subarray if it contains duplicates
        for i in range(k+1, len(nums)):
            unique_set.remove(nums[i-k-1])
            # Check if the curr element is already present in set
            if nums[i] in unique_set:
                return True
            else:
                unique_set.add(nums[i])
        
        return False
        
        