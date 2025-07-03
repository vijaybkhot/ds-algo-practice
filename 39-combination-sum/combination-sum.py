class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        # candidates.sort()
        def dfs(start, path):
            if sum(path) == target:
                res.append(path[::])
                return

            if start == len(candidates) or sum(path) > target:
                return
            
            # for i in range(start, len(candidates)):
            #     path.append(candidates[i])
            #     dfs(i, path)
            #     path.pop()

            # Include current num
            path.append(candidates[start])
            dfs(start, path)
            path.pop()
            # skip current num
            dfs(start+1, path)
        
        dfs(0, [])
        return res

















        
        # # result = []
        # # def dfs(start_index, current_combination, total):
        # #     if total == target:
        # #         result.append(current_combination.copy())
        # #         return
        # #     if start_index >= len(candidates) or total > target:
        # #         return

        # #     # Considering the current start_index
        # #     # Include current number
        # #     current_combination.append(candidates[start_index])
        # #     dfs(start_index, current_combination, total + candidates[start_index])
        # #     current_combination.pop()

        # #     # Exclude current number
        # #     dfs(start_index + 1, current_combination, total)
        
        # # dfs(0, [], 0)
        # # return result

        # # ## Sorting and using a for loop to backtrack
        # # result = []
        # # candidates.sort()  

        # # def dfs(start_index, current_combination, remaining_target):
        # #     if remaining_target == 0:
        # #         result.append(current_combination[:])
        # #         return

        # #     for i in range(start_index, len(candidates)):
        # #         if candidates[i] > remaining_target:
        # #             break  # No point in continuing if candidate is too large

        # #         # Include candidates[i] and stay at i (can reuse the same number)
        # #         current_combination.append(candidates[i])
        # #         dfs(i, current_combination, remaining_target - candidates[i])
        # #         current_combination.pop()  # backtrack

        # # dfs(0, [], target)
        # # return result

        # res= []
        # candidates.sort()
        # def dfs(index, curr_path, total):
        #     if total == target:
        #         res.append(curr_path[:])
        #         return
        #     if total > target:
        #         return
            
        #     for i in range(index, len(candidates)):
        #         if candidates[i] > target:
        #             break
        #         if total + candidates[i] <= target:
        #             curr_path.append(candidates[i])
        #             dfs(i, curr_path, total+candidates[i])
        #             curr_path.pop()
        # dfs(0, [], 0)
        # return res

