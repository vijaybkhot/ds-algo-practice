class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0

        for i in range(32):
            bit = (n >> i) & 1  # Get the i-th bit . Shift n to the right by i
            res = res | (bit << (31-i))
        
        return res