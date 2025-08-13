class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        x = 1
        while x <= n:
            if x == n:
                return True
            x *= 3

        return False