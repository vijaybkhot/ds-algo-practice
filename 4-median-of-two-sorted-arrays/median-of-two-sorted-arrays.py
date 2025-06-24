class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        if i < len(nums1):
            merged.extend(nums1[i:])

        if j < len(nums2):
            merged.extend(nums2[j:])
        
        if len(merged) % 2:
            return merged[len(merged)//2]
        else:
            mid = len(merged) // 2
            return (merged[mid]+merged[mid-1]) / 2

        