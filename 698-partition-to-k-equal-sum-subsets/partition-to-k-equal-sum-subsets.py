class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # total_sum = sum(nums)
        # if total_sum % k or len(nums) < k:
        #     return False
        # target_subset_sum = total_sum // k
        
        # nums.sort(reverse=True)
        # subsets = [0] * k
        # def dfs(index):
        #     if index == len(nums):
        #         return all(subset == target_subset_sum for subset in subsets)
            
        #     for i in range(k):
        #         if subsets[i] + nums[index] <= target_subset_sum:
        #             subsets[i] += nums[index]
        #             if dfs(index+1):
        #                 return True
        #             subsets[i] -= nums[index]

        #         if subsets[i] == 0:
        #             break
        #     return False
        
        # return dfs(0)

        # total_sum = sum(nums)
        # if total_sum % k or len(nums) < k:
        #     return False

        # target = total_sum // k
        # nums.sort(reverse=True)  # Start with largest numbers
        # visited = [False] * len(nums)

        # def backtrack(start_index, subset_index, current_sum):
        #     # If we've filled k - 1 subsets successfully, the last one must be valid
        #     if subset_index == k - 1:
        #         return True

        #     # When a subset is complete, start the next one
        #     if current_sum == target:
        #         return backtrack(0, subset_index + 1, 0)

        #     for i in range(start_index, len(nums)):
        #         if not visited[i] and current_sum + nums[i] <= target:
        #             visited[i] = True
        #             if backtrack(i + 1, subset_index, current_sum + nums[i]):
        #                 return True
        #             visited[i] = False  # backtrack

        #             #Prune if the current subset is empty — no need to try other elements at this level
        #             if current_sum == 0:
        #                 break

        #     return False

        # return backtrack(0, 0, 0)

        total_sum = sum(nums)
        if total_sum % k:
            return False
        
        target_sub_sum = total_sum//k
        subs = [0] * k
        nums.sort(reverse=True)
        # def dfs(start):
        #     if start == len(nums):
        #         return all(sub == target_sub_sum for sub in subs)

        #     for i in range(k):
        #         if nums[start] + subs[i] <= target_sub_sum:
        #             subs[i] += nums[start]
        #             if dfs(start+1):
        #                 return True
        #             subs[i] -= nums[start]
                
        #         if subs[i] == 0:
        #             return False
        #     return False
        
        # return dfs(0)
        visited = [False] * len(nums)
        def dfs(start, sub_index, curr_sub_total):
            if sub_index == k-1:
                return True
            
            if curr_sub_total == target_sub_sum:
                return dfs(0, sub_index+1, 0)
            
            for i in range(start, len(nums)):
                if not visited[i] and nums[i] + curr_sub_total <= target_sub_sum:
                    visited[i] = True
                    if dfs(i+1, sub_index, curr_sub_total+nums[i]):
                        return True
                    visited[i] = False
                    if curr_sub_total == 0:
                        break
            return False
        
        return dfs(0, 0, 0)




        