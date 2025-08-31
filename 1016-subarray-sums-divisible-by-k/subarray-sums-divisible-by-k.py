class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        remainder_count = defaultdict(int)
        remainder_count[0] = 1

        curr_sum = 0
        num_subarrays = 0

        for idx, num in enumerate(nums):
            curr_sum += num
            if curr_sum % k in remainder_count:
                num_subarrays += remainder_count[curr_sum % k]
            remainder_count[curr_sum % k] += 1
        
        return num_subarrays