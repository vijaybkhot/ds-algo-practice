class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []

        def dfs(i, path):
            if len(path) == k:
                result.append(path[:])
                return 
            if len(path) > k:
                return
            if i <= n:
                path.append(i)
                dfs(i+1, path)
                path.pop()
                dfs(i+1, path)
        
        dfs(1, [])
        return result
        