class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # e  l   e   e   t   m   i   n   i   c   o   w  o    r   o   e   p
        # 1  1   2   3    3  3   4   4   5    5  6   6  7    7   8   9   9
        #    0   1   2    2  2   3   3   4    4  5   5  6    6   7   8   8

        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        mask = 0 
        seen = {0: -1}
        res = 0

        for idx, ch in enumerate(s):
            if ch in vowel_to_bit:
                bit = vowel_to_bit[ch]
                mask ^= (1 << bit)
            if mask in seen:
                res = max(res, idx-seen[mask])
            else:
                seen[mask] = idx
        
        return res