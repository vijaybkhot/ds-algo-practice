class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums2)
        stack = []
        for index, num in enumerate(nums2):
            while stack and stack[-1][0] < num:
                stack_num, stack_idx = stack.pop()
                res[stack_idx] = num
            stack.append([num, index])
        output = []
        for num in nums1:
            idx = nums2.index(num)
            output.append(res[idx])
        return output

        