class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i*i <= n:
            square = i*i
            squares.append(square)
            i += 1
        
        # squares = squares[::-1]

        # self.min_count = n
        # memo = {}
        # def dfs(path, curr_sum):
        #     if curr_sum in memo and path >= memo[curr_sum]:
        #         return
        #     if curr_sum == n:
        #         self.min_count = min(self.min_count, path)
        #         return
            
        #     if curr_sum > n:
        #         return
        
        #     for num in squares:
        #         dfs(path+1, curr_sum+num)

        #     memo[curr_sum] = min(memo.get(curr_sum, float('inf')), path)

        # def dfs(path, curr_sum):
        #     if curr_sum == n:
        #         self.min_count = min(self.min_count, path)
        #         return

        #     if curr_sum > n:
        #         return

        #     # Only explore deeper if this path to curr_sum is better (shorter)
        #     if curr_sum not in memo or path < memo[curr_sum]:
        #         memo[curr_sum] = path
        #         for num in squares:
        #             dfs(path + 1, curr_sum + num)
        
        # dfs(0, 0)
        # return self.min_count

        # # Using bottom-up DP - Came up with this solution without external help
        # dp = [n]*(n+1)
        # dp[0] = 0
        
        # for i in range(1, n+1):
        #     j = 0
        #     while j < len(squares) and squares[j] <= i:
        #         curr_square = squares[j]
        #         last_dp_idx = i - curr_square
        #         last_dp_min_count = dp[last_dp_idx]
        #         dp[i] = min(dp[i], last_dp_min_count+1)
        #         j += 1
        # return dp[n]

        # Using BFS to explore all sum nodes
        q = deque()
        seen = set()
        
        res = 0
        q.append(0)
        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                s = 1
                while s * s + cur <= n:
                    nxt = cur + s * s
                    if nxt == n:
                        return res
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append(nxt)
                    s += 1
                    
        return res



        