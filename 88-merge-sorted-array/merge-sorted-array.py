class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # # Solution using an extra array: O(n) time and space complexity
        # nums3 = nums1[:]
        # i, j, k = 0, 0, 0

        # while i < m and j < n:
        #     if nums3[i] < nums2[j]:
        #         nums1[k] = nums3[i]
        #         k += 1
        #         i += 1
        #     else:
        #         nums1[k] = nums2[j]
        #         k += 1
        #         j += 1
        # while i < m:
        #     nums1[k] = nums3[i]
        #     k += 1
        #     i += 1
        # while j < n:
        #     nums1[k] = nums2[j]
        #     k += 1
        #     j += 1

        # In-place merging without an extra array - O(n) time and O(1) space complexity

        last = m + n -1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1

