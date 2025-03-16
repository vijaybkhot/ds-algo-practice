class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # # Brute force approach. O(m+n)
        # # Merge the two arrays
        # nums = [0] * (len(nums1) + len(nums2))
        # i, j, k = 0, 0, 0

        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         nums[k] = nums1[i]
        #         i += 1
        #     else:
        #         nums[k] = nums2[j]
        #         j += 1
        #     k += 1
        
        # while i < len(nums1):
        #     nums[k] = nums1[i]
        #     i += 1
        #     k += 1
        # while j < len(nums2):
        #     nums[k] = nums2[j]
        #     j += 1
        #     k += 1
        

        # mid = len(nums) // 2
        # if len(nums) % 2 == 0:
        #     return float(nums[mid-1]+nums[mid]) / 2
        # else:
        #     return nums[mid]

        # Optimized approach using binary search without merging the two arrays
        # Ensure the first array is the smaller one
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return float(max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1