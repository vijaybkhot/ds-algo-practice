class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #   2   3   4   -1  -1
        #             -1     4
        #  [1,  2,  3,  4,  3]

        n = len(nums)
        res = [-1]* n
        

        stack = []  #(num, idx)

        for i in range(2*n):
            num = nums[i%n]
            while stack and stack[-1][0] < num:
                back_num, back_idx = stack.pop()
                res[back_idx] = num
            if i < n:
                stack.append((num, i))

        
        return res