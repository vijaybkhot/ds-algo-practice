class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r, k = m-1, n-1, len(nums1)-1

        while l >= 0 and r >=0:

            if nums1[l] > nums2[r]:
                nums1[k] = nums1[l]
                l -= 1
            else:
                nums1[k] = nums2[r]
                r -= 1
            k -= 1
        
        while r >= 0:
            nums1[k] = nums2[r]
            r -= 1
            k -= 1
