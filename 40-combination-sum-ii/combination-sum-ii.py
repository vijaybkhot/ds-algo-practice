class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ## Brute Force approach
        # result = []
        # def dfs(curr_index, curr_combination, total):
        #     if total == target:
        #         append_copy = curr_combination.copy()
        #         curr_set = set(append_copy)
        #         if len(append_copy) != len(curr_set):
        #             curr_copy = sorted(append_copy)
        #             if curr_copy not in result:
        #                 result.append(curr_copy)
        #         else:
        #         if curr_set not in result:
        #             result.append(curr_set)

        #         return
        #     if total > target or curr_index >= len(candidates):
        #         return
            
        #     curr_combination.append(candidates[curr_index])
        #     dfs(curr_index+1, curr_combination, total+candidates[curr_index])
        #     curr_combination.pop()
        #     dfs(curr_index+1, curr_combination, total)
        
        # dfs(0, [], 0)
        # return [list(res) for res in result]

        # Optimized approach using sorting
        candidates.sort()
        result = []
        def dfs(curr_index, curr_combination, total):
            if total == target:
                result.append(curr_combination[:])
                return
            if total > target or curr_index >= len(candidates):
                return
            
            curr_combination.append(candidates[curr_index])
            dfs(curr_index+1, curr_combination, total + candidates[curr_index])
            curr_combination.pop()
            new_curr_index = curr_index + 1
            while new_curr_index  < len(candidates) and candidates[new_curr_index-1] == candidates[new_curr_index]:
                new_curr_index += 1
            dfs(new_curr_index, curr_combination, total)
        
        dfs(0, [], 0)
        return result


        