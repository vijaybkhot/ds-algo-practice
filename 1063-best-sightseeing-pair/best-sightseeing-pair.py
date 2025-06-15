class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        # res = float('-inf')
        # # Brute force approach
        # for i in range(len(values)):
        #     for j in range(i+1, len(values)):
        #         curr_cost = values[i] + values[j] + i - j
        #         res = max(res, curr_cost)
        
        # return res
        # n = len(values)
        # dp = [0]*n
        # max_num = max(values)
        # max_idx = values.index(max_num)
        # dp[max_idx] = values[max_idx]
        # for j in range(max_idx+1, n):
        #     dp[j] = values[j] + max_num + max_idx - j
        
        # for i in range(0, max_idx):
        #     dp[i] = values[i] + max_num + i - max_idx
        
        # return max(dp)
        curr_max_left = values[0] + 0
        curr_min_right = values[1] - 1

        res = curr_max_left + curr_min_right
        j = 1
        for j in range(1, len(values)):
            res = max(res, curr_max_left + values[j] - j)
            curr_max_left = max(curr_max_left, values[j] + j)
        
        return res

        

        