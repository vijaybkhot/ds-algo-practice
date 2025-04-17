class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k or len(nums) < k:
            return False
        target_subset_sum = total_sum // k

        subsets = [0] * k
        def dfs(index):
            if index == len(nums):
                return all(subset == target_subset_sum for subset in subsets)
            
            for i in range(k):
                if subsets[i] + nums[index] <= target_subset_sum:
                    subsets[i] += nums[index]
                    if dfs(index+1):
                        return True
                    subsets[i] -= nums[index]
                    
                if subsets[i] == 0:
                    break
            return False
        
        return dfs(0)
        