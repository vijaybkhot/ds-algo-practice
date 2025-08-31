class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        goal = sum(nums) - x
        if goal < 0:
            return -1
        n = len(nums)
        if goal == 0:
            return n
        
        pre_map = {0: -1}  # prefix sum -> earliest index
        curr_sum = 0
        res = -1
        

        for idx, num in enumerate(nums):
            curr_sum += num
            if curr_sum - goal in pre_map:
                res = max(res, idx - pre_map[curr_sum - goal])
            if curr_sum not in pre_map:  # store earliest occurrence
                pre_map[curr_sum] = idx

        return n - res if res != -1 else -1