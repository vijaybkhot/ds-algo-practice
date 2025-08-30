class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #   1, 1, 1
        #  0,  1, 2, 3

        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        prefix_sum = 0
        count = 0

        for idx, num in enumerate(nums):
            curr_sum = prefix_sum+num
            if curr_sum-k in prefix_map:
                count += prefix_map[curr_sum-k]
            prefix_sum = curr_sum
            prefix_map[prefix_sum] += 1
        
        return count