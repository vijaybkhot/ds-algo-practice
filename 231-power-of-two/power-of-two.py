class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def count_set_bits(n):
            count = 0
            while n:
                count += n & 1  # check last bit
                n >>= 1         # shift right
            return count

        return n > 0 and count_set_bits(n) == 1