class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def isValidSubArraysForSum(sum_to_check, array, k):
            current_sum = 0
            subarray_count = 1  # Start with the first subarray

            for num in array:
                if current_sum + num > sum_to_check:
                    # If adding this num would exceed sum_to_check, start a new subarray
                    subarray_count += 1
                    current_sum = num
                    # If we have more than k subarrays, return False
                    if subarray_count > k:
                        return False
                else:
                    # Otherwise, add num to the current subarray sum
                    current_sum += num

            # If we used exactly k subarrays, return True, else return False
            return subarray_count <= k

        largest_sum = sum(nums)
        low, high = max(nums), sum(nums)
        while low <= high:
            mid = (low + high) // 2
            if isValidSubArraysForSum(mid, nums, k):
                largest_sum = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return largest_sum


                    


                    
            