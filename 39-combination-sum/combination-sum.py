class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr_candidates):
            if i == len(candidates):
                return 0
            
            curr_sum = sum(curr_candidates)
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(curr_candidates[::])
                return 
            
            # take
            curr_candidates.append(candidates[i])
            dfs(i, curr_candidates)
            curr_candidates.pop()
            dfs(i+1, curr_candidates)
        
        dfs(0, [])
        return res
