class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
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

        def dfs(start_index, current_combination, total):
            if total == target:
                result.append(current_combination.copy())
                return
            if start_index >= len(candidates) or total > target:
                return

            # Considering the current start_index
            # Include current number
            current_combination.append(candidates[start_index])
            dfs(start_index, current_combination, total + candidates[start_index])
            current_combination.pop()

            # Exclude current number
            dfs(start_index + 1, current_combination, total)
        
        dfs(0, [], 0)
        return result
