class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def isCapabale(capability):
            i = 0
            valid_houses = 0
            while i < len(nums):
                if nums[i] <= capability:
                    i += 2
                    valid_houses += 1
                else:
                    i += 1
                if valid_houses == k:
                    break
            
            return valid_houses == k

        low, high = min(nums), max(nums)
        res = 0

        while low <= high:
            mid = (low + high) // 2
            if isCapabale(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res

        