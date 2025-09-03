class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        rem_map = defaultdict(int)
        rem_map[0] = 1
        curr_sum = 0
        res = 0
        for idx, num in enumerate(nums):
            curr_sum += num
            remainder = curr_sum%k
            if remainder in rem_map:
                res += rem_map[remainder]
            
            rem_map[remainder] += 1
        
        return res