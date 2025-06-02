class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i*i <= n:
            square = i*i
            squares.append(square)
            i += 1
        
        squares = squares[::-1]

        self.min_count = n
        memo = {}
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

        def dfs(path, curr_sum):
            if curr_sum == n:
                self.min_count = min(self.min_count, path)
                return

            if curr_sum > n:
                return

            # Only explore deeper if this path to curr_sum is better (shorter)
            if curr_sum not in memo or path < memo[curr_sum]:
                memo[curr_sum] = path
                for num in squares:
                    dfs(path + 1, curr_sum + num)
        
        dfs(0, 0)
        return self.min_count


        