class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1
            while left <= right and counter[0] > k:
                counter[nums[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)
        
        return res
