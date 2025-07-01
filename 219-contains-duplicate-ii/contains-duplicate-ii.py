class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = defaultdict(int)
        for i in range(0, min(len(nums), k+1)):
            counter[nums[i]] += 1
            if counter[nums[i]] > 1:
                return True
        
        for i in range(k+1, len(nums)):
            counter[nums[i-k-1]] -= 1
            counter[nums[i]] += 1
            if counter[nums[i]] > 1:
                return True
        
        return False
        