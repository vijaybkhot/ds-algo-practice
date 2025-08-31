class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # [0,   1,  0,  1]
        #  1,   1,  2,  2
        #   0,  1,  1,  2
        #   1,  0,  

        diff_map = defaultdict(int)
        diff_map[0] = -1
        zero, one = 0, 0
        res = 0
        for idx, num in enumerate(nums):
            if num:
                one += 1
            else:
                zero += 1
            diff = zero-one

            if diff in diff_map:
                res = max(res, idx - diff_map[diff])
            else:
                diff_map[diff] = idx
        
        return res
