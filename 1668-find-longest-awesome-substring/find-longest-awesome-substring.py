class Solution:
    def longestAwesome(self, s: str) -> int:

        def count_set_bits_shift(n: int) -> int:
            count = 0
            while n:
                count += (n & 1)  
                n >>= 1           
            return count

        seen = {0:-1}
        mask = 0
        res = 0
        for i, digit in enumerate(s):
            digit = int(digit)
            mask ^= (1 << digit)

            # Case 1: whole substring is awesome
            if mask in seen:
                res = max(res, i - seen[mask])
            else:
                seen[mask] = i
            
            # Case 2: substring differs by one bit (one odd digit allowed)
            for d in range(10):
                new_mask = mask ^ (1 << d)
                if new_mask in seen:
                    res = max(res, i - seen[new_mask])
        
        return res


