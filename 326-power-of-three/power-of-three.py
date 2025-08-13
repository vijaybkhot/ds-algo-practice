class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # x = 1
        # while x <= n:
        #     if x == n:
        #         return True
        #     x *= 3

        # return False
        e=log(1<<31)/log(3)//1
        N=pow(3, e)
        return n>0 and N%n==0