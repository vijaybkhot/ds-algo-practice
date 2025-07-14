class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        # # Solution - I
        # for i in range(32):
        #     bit = (n >> i) & 1  # Shift n to the right by i and  get the i-th bit from left .
        #     res = res | (bit << (31-i)) # Take the current bit and place it at position (31 - i) in the result integer res.

        # Solution - II - More readable
        for i in range(32):
            res = (res << 1) | (n & 1)
            n = n >> 1
        
        return res