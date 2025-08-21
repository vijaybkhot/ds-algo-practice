class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []  #(num, index)
        next_greater = defaultdict(int)
        for i in range(len(nums2)):
            curr_num = nums2[i]
            while stack and stack[-1][0] < curr_num:
                num, index = stack.pop()
                next_greater[num] = curr_num
            stack.append((curr_num, i))

        res = []
        for num in nums1:
            if next_greater[num] > 0:
                res.append(next_greater[num])
            else:
                res.append(-1)
        
        return res
                