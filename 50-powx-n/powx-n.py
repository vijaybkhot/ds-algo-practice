class Solution:
    def myPow(self, x: float, n: int) -> float:
        # multiplier = x
        # if n == 0:
        #     return 1
        
        # for i in range(1, abs(n)):
        #     x *= multiplier
        

        # return x if n >= 0 else 1/x
        def recursive_helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = recursive_helper(x, n//2)
            res = res * res
            return x * res if n%2 else res
                
        
        res = recursive_helper(x, abs(n))

        return res if n >= 0 else 1/res