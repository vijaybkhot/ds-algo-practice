class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        # sum_1 = sum(nums1)
        # sum_2 = sum(nums2)


        # if sum_2 > sum_1:
        #     nums1, nums2 = nums2, nums1
        #     sum_2, sum_1 = sum_1, sum_2
        

        # nums_freq_1 = Counter(nums1)
        # nums_freq_2 = Counter(nums2)

        # if sum_1 == sum_2 and nums_freq_1[0] == nums_freq_2[0]:
        #     return sum_1 + (nums_freq_1[0] * 1)

        # if sum_1 == sum_2 and nums_freq_1[0] < nums_freq_2[0]:
        #     nums_freq_1, nums_freq_2 = nums_freq_2, nums_freq_1



        # min_sum_1 = sum_1 + (nums_freq_1[0] * 1)
        # min_sum_2 = sum_2 + (nums_freq_2[0] * 1)

        # if min_sum_1 >= min_sum_2:
        #     return min_sum_1 if nums_freq_2[0] > 0 and nums_freq_2[0] <= min_sum_1-sum_2   else -1
        # else:
        #     return min_sum_2 if nums_freq_1[0] > 0 and nums_freq_1[0] <= min_sum_2-sum_1   else -1
        
        # sum_1 = sum(nums1)
        # sum_2 = sum(nums2)
        

        # nums_freq_1 = Counter(nums1)
        # nums_freq_2 = Counter(nums2)

        # if sum_1 == sum_2 and nums_freq_1[0] == nums_freq_2[0]:
        #     return sum_1 + (nums_freq_1[0] * 1)
        
        # if nums_freq_2[0] > nums_freq_1[0]:
        #     nums_freq_1, nums_freq_2 = nums_freq_2, nums_freq_1
        #     sum_1, sum_2 = sum_2, sum_1
        
        # while nums_freq_1[0] > 0 and nums_freq_2[0] > 0:
        #     sum_1 += 1
        #     nums_freq_1[0] -= 1
        #     sum_2 += 1
        #     nums_freq_2[0] -= 1

        # if nums_freq_1[0] > 0 and sum_1 < sum_2 and nums_freq_1[0] <= sum_2-sum_1:
        #     return sum_2
        # else:
        #     return -1
        
        

        sum1, sum2 = sum(nums1), sum(nums2)
        zero1, zero2 = nums1.count(0), nums2.count(0)

        # If already equal and zero counts are same
        if sum1 == sum2 and zero1 == zero2:
            return sum1 + zero1

        # Ensure nums1 is the one with smaller sum
        if sum1 + (zero1 * 1) > sum2 + (zero2 * 1):
            sum1, sum2 = sum2, sum1
            zero1, zero2 = zero2, zero1

        # We need to increase sum1 by (sum2 - sum1)
        diff = sum2 + (zero2 * 1) - sum1
        if zero1 == 0 or zero1 > diff:
            return -1
        
        # We can balance by using exactly `diff` zeros
        return sum2 + (zero2 * 1)