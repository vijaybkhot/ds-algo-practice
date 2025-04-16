class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        # # Brute force - incorrect approach
        # matchsticks.sort()
        # def dfs(start, path, side):
        #     if start >= n:
        #         return True if path == 4 else False
        #     curr_side = 0
        #     i = start
        #     while i < n and curr_side < side:
        #         curr_side += matchsticks[i]
        #         i += 1
        #     if curr_side != side or n - i < 4 - (path+1):
        #         return False

        #     return dfs(i, path+1, side)
        
        
        # if not matchsticks:
        #     return False

        # min_stick = matchsticks[0]
        # max_stick = matchsticks[-1]

        # for side_len in range(min_stick, max_stick+1, 1):
        #     if dfs(0, 0, side_len):
        #         return True
        
        # return False
                 
            
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        target_side = total // 4
        matchsticks.sort(reverse=True)  # Start with bigger sticks to prune faster
        sides = [0] * 4

        def dfs(index):
            if index == len(matchsticks):
                return all(side == target_side for side in sides)
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= target_side:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                    
                # Optimization: If this side is still 0 after trying,
                # don't try placing it in other empty sides
                if sides[i] == 0:
                    break
                    
            return False

        return dfs(0)