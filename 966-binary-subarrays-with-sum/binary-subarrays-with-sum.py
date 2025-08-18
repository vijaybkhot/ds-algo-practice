class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
      
        # prefix_map = defaultdict(int)
        # prefix_map[0] = 1
        # prefix = 0
        # count = 0

        # for idx, num in enumerate(nums):
        #     prefix += num
        #     if prefix-goal in prefix_map:
        #         count += prefix_map[prefix-goal]
        #     prefix_map[prefix] += 1
        
        # return count
        return self.atMostGoal(nums, goal) - self.atMostGoal(nums, goal-1)
    def atMostGoal(self, nums, goal):
        count = 0
        left = 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]

            while left <= right and total > goal:
                total -= nums[left]
                left += 1
            count += right - left + 1

        return count
