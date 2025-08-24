class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0]*n

        stack = []
        for idx, num in enumerate(heights):
            while stack and stack[-1][0] < num:
                _, i = stack.pop()
                res[i] += 1
            if stack:
                res[stack[-1][1]] += 1
            stack.append((num, idx))
        
        return res
