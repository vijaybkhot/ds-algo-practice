class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Brute force approach
        # Merge the two arrays
        nums = [0] * (len(nums1) + len(nums2))
        i, j, k = 0, 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1
        
        while i < len(nums1):
            nums[k] = nums1[i]
            i += 1
            k += 1
        while j < len(nums2):
            nums[k] = nums2[j]
            j += 1
            k += 1
        

        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            return float(nums[mid-1]+nums[mid]) / 2
        else:
            return nums[mid]


        