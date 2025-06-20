class Solution:
    def fib(self, n: int) -> int:
        dp_0, dp_1 = 0, 1

        if n < 2:
            return n

        for i in range(2, n+1):
            new_dp = dp_0 + dp_1
            dp_0 = dp_1
            dp_1 = new_dp

        return dp_1        