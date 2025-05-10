class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        sum_1 = sum(nums1)
        sum_2 = sum(nums2)


        if sum_2 > sum_1:
            nums1, nums2 = nums2, nums1
            sum_2, sum_1 = sum_1, sum_2
        

        

        nums_freq_1 = Counter(nums1)
        nums_freq_2 = Counter(nums2)

        if sum_1 == sum_2 and nums_freq_1[0] == nums_freq_2[0]:
            return sum_1 + (nums_freq_1[0] * 1)

        if sum_1 == sum_2 and nums_freq_1[0] < nums_freq_2[0]:
            nums_freq_1, nums_freq_2 = nums_freq_2, nums_freq_1



        min_sum_1 = sum_1 + (nums_freq_1[0] * 1)
        min_sum_2 = sum_2 + (nums_freq_2[0] * 1)

        if min_sum_1 >= min_sum_2:
            return min_sum_1 if nums_freq_2[0] > 0 and nums_freq_2[0] <= min_sum_1-sum_2   else -1
        else:
            return min_sum_2 if nums_freq_1[0] > 0 and nums_freq_1[0] <= min_sum_2-sum_1   else -1
        