class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        # 
        # [ 18,   52,  -]
        #              ^
        #               ^
        #  0    1   2   3   4   5   6   7   8   9   10  11
        # [71,  18, 52, 29, 55, 73, 24, 42, 66, 8,  80, 2]
        for idx, num in enumerate(nums):
            while stack and stack[-1] > num and n-idx >= k-len(stack)+1:
                stack.pop()
            stack.append(num)
    
        return stack[:k]