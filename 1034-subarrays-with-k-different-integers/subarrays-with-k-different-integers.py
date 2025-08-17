class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # {1: 2, 2: 2, 3: 1}
        #  l                r
        # [1,   2,  3,  1,  2]
        # num_set = defaultdict(int)
        # count = 0
        # for right in range(len(nums)):
        #     num_set[nums[right]] += 1
        #     temp_set = num_set.copy()
        #     left = 0
        #     while right - left + 1 >= k and len(temp_set) > k:
        #         temp_set[nums[left]] -= 1
        #         if temp_set[nums[left]] == 0:
        #             del temp_set[nums[left]]
        #         left += 1
        #     while right - left + 1 >= k and len(temp_set) == k:
        #         count += 1
        #         temp_set[nums[left]] -= 1
        #         if temp_set[nums[left]] == 0:
        #             del temp_set[nums[left]]
        #         left += 1

        # return count


        # Optimized approach
        return self.atMostK(nums, k) - self.atMostK(nums, k-1)
    def atMostK(self, nums, k):
        count = 0
        left = 0
        freq = defaultdict(int)
        for right in range(len(nums)):
            freq[nums[right]] += 1
            while len(freq) > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            count += right - left + 1
        
        return count
    

