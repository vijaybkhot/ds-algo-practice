class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merged = []
        # i, j = 0, 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         merged.append(nums1[i])
        #         i += 1
        #     else:
        #         merged.append(nums2[j])
        #         j += 1
        # if i < len(nums1):
        #     merged.extend(nums1[i:])

        # if j < len(nums2):
        #     merged.extend(nums2[j:])
        
        # if len(merged) % 2:
        #     return merged[len(merged)//2]
        # else:
        #     mid = len(merged) // 2
        #     return (merged[mid]+merged[mid-1]) / 2

        # Using binary seach to find the left partition:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1) + len(nums2)
        odd = n % 2 == 1
        left, right = 0, len(nums1)

        while left <= right:
            i = (left + right) // 2
            j = (n + 1) // 2 - i

            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == len(nums1) else nums1[i]
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == len(nums2) else nums2[j]

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if odd:
                    return max(nums1_left_max, nums2_left_max)
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1
                

                        


                