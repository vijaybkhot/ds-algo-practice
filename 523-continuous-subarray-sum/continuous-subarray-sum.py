class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 23,   2,  6,  4,  7
        # 23,   25, 31, 35, 42
        # 5:0, 1:1, 
        prefix_map = {0: -1} 
        prefix_map[0] = -1
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            rem = curr_sum % k

            if rem in prefix_map:
                if i - prefix_map[rem] >= 2:
                    return True
            else:
                prefix_map[rem] = i

        return False
        