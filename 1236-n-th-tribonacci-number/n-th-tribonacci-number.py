class Solution:
    def tribonacci(self, n: int) -> int:

        # # Simple recursion 
        # def tribonacci(n):
        #     if n == 0:
        #         return 0
        #     elif n == 1 or n == 2:
        #         return 1
        #     return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
        
        # return tribonacci(n)

        # # Library Memoized recursion 
        # @lru_cache(maxsize=None)
        # def tribonacci(n):
        #     if n == 0:
        #         return 0
        #     elif n == 1 or n == 2:
        #         return 1
        #     return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
        
        # return tribonacci(n)

        # Manual memoization

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        memo = [-1]*(n+1)
        memo[0], memo[1], memo[2] = 0, 1, 1

        def tribo(n):
            if memo[n] != -1:
                return memo[n]
            
            memo[n] = tribo(n-1) + tribo(n-2) + tribo(n-3)
            return memo[n]
        
        return tribo(n)



        # if n == 0:
        #     return 0
        # elif 1 <= n <= 2:
        #     return 1
        # t_0, t_1, t_2 = 0, 1, 1
        # for i in range(3, n+1):
        #     t_3 = t_0 + t_1 + t_2
        #     t_0 = t_1
        #     t_1 = t_2
        #     t_2 = t_3
        
        # return t_2
        