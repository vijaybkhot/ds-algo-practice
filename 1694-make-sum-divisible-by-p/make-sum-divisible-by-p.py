class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        # target = (sum(nums))%p
        # left = 0
        # curr_sum = 0
        # res = float('inf')
        # for right in range(len(nums)):
        #     curr_sum += nums[right]

        #     while left <= right and curr_sum > target:
        #         curr_sum -= nums[left]
        #         left += 1
        #     if curr_sum == target:
        #         res = min(res, right-left+1)
        
        # return res if res < len(nums) else -1
    
        # [3,   1,  4,  2]
        #  ^
        # sum = 4
        # {0: -1}
        # res = 5
        # target = 4

        target = (sum(nums))%p
        curr_sum = 0
        pre_map = defaultdict(int)
        pre_map[0] = -1
        res = float('inf')
        if target == 0:
            return 0
        for idx, num in enumerate(nums):
            curr_sum += num
            mod = curr_sum%p

            if (mod-target) % p in pre_map:
                res = min(res, idx-pre_map[(mod-target) % p])
            
            pre_map[mod] = idx

        
        return res if res < len(nums) else -1