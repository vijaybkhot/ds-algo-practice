class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = dict()

        for idx, num in enumerate(nums):
            if num in num_map and abs(num_map[num]-idx) <= k:
                return True
            num_map[num] = idx
        return False