class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[0] != '0' or s[-1] != '0':
            return False

        # farthest = 0
        # earliest = 0
        # i = 0
        # while i < n:
        #     while i < farthest and s[i]!= '0':
        #         i += 1
        #     if i < n-1 and s[i] != '0':
        #         return False
        #     farthest = max(farthest, i + maxJump)  
        #     if i <= n-1 and farthest >= n-1:
        #         return True
        #     i = i+minJump
        #     if i >= n:
        #         return False

        # return True                

        # # Using BFS
        # q = deque()
        # q.append(0)
        # farthest = 0

        # while q:
        #     curr = q.popleft()
        #     if curr >= n-1:
        #         return True
        #     start = max(curr+minJump, farthest + 1)
        #     for j in range(start, min(curr + maxJump + 1, n)):
        #         if j < n and s[j] == '0':
        #             q.append(j)
                
        #     farthest = curr + maxJump
        
        # return False

        # DP two pointer approach
        dp = [False]*n
        dp[0] = True
        j = 0
        for i in range(n):
            if not dp[i]:
                continue
            
            j = max(j, i+minJump)
            while j < min(i+maxJump+1, n):
                if s[j] == '0':
                    dp[j] = True
                j += 1
        
        return dp[n-1]
                


        