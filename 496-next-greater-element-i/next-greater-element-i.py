class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Solution without external help
        # Using monotonically decreasing stack approach
        # res = [-1] * len(nums2)
        # stack = []
        # for index, num in enumerate(nums2):
        #     while stack and stack[-1][0] < num:
        #         stack_num, stack_idx = stack.pop()
        #         res[stack_idx] = num
        #     stack.append([num, index])
        # output = []
        # for num in nums1:
        #     idx = nums2.index(num)
        #     output.append(res[idx])
        # return output

        # More optimal solution.# Instead of using the index() method O(n), to get index of an element in array, We can create a index map to lookup index in O(1)
        index_map = {}
        for index, num in enumerate(nums2):
            index_map[num] = index
        
        next_greater = [-1] * len(nums2)
        stack = []
        for index, num in enumerate(nums2):
            while stack and stack[-1][0] < num:
                stack_num, stack_idx = stack.pop()
                next_greater[stack_idx] = num
            stack.append([num, index])
        output = []
        for num in nums1:
            output.append(next_greater[index_map[num]])
        return output

        