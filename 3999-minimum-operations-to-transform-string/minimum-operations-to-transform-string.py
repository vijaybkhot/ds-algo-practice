class Solution:
    def minOperations(self, s: str) -> int:
        
        # min_char = 26
        # for char in s:
        #     if char == 'a':
        #         continue
        #     min_char = min(min_char, ord(char) - ord('a'))
        
        # if min_char == 26:
        #     return 0
        
        # num_operations = 26 - min_char

        # return num_operations if min_char else 0

        max_ops = 0
        for ch in s:
            dist = (26 - (ord(ch) - ord('a'))) % 26
            max_ops = max(max_ops, dist)
        return max_ops