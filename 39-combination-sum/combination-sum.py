class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # result = []
        # def dfs(start_index, current_combination, total):
        #     if total == target:
        #         result.append(current_combination.copy())
        #         return
        #     if start_index >= len(candidates) or total > target:
        #         return

        #     # Considering the current start_index
        #     # Include current number
        #     current_combination.append(candidates[start_index])
        #     dfs(start_index, current_combination, total + candidates[start_index])
        #     current_combination.pop()

        #     # Exclude current number
        #     dfs(start_index + 1, current_combination, total)
        
        # dfs(0, [], 0)
        # return result

        ## Sorting and using a for loop to backtrack

        result = []
        candidates.sort()  # Sorting helps with early stopping

        def dfs(start_index, current_combination, remaining_target):
            if remaining_target == 0:
                result.append(current_combination[:])
                return

            for i in range(start_index, len(candidates)):
                if candidates[i] > remaining_target:
                    break  # No point in continuing if candidate is too large

                # Include candidates[i] and stay at i (can reuse the same number)
                current_combination.append(candidates[i])
                dfs(i, current_combination, remaining_target - candidates[i])
                current_combination.pop()  # backtrack

        dfs(0, [], target)
        return result
