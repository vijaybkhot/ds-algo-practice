class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0]*n

        # (11, 4)
        # 3,    1,  2,  1,  0,  0
        #                       ^
        # 10,   6,  8,  5,  11, 9


        stack = []
        for idx, num in enumerate(heights):
            while stack and stack[-1][0] < num:
                _, i = stack.pop()
                res[i] += 1
            if stack:
                res[stack[-1][1]] += 1
            stack.append((num, idx))
        
        return res
