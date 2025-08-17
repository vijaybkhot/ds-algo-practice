class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # n = 4
        # res = [[12], [13], ]
        # 1, ""
        # 2, "1" / 2, ""
        # 3, "12" / 3, "1" // 3, "2"/ 3, ""
        # 4, "1" // 4, "23" / 4, "2" // 4, "3" / 4, ""

        
        res = []
        def dfs(i, curr_comb):
            if len(curr_comb) == k:
                res.append(curr_comb[::])
                return
            if i >= n+1:
                return

            curr_comb.append(i)
            # take curr num
            dfs(i+1, curr_comb)
            # skip curr num
            curr_comb.pop()
            dfs(i+1, curr_comb)
        
        dfs(1, [])
        return res