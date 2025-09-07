class Solution:
    def minOperations(self, s: str) -> int:
        
        min_char = 26
        for char in s:
            if char == 'a':
                continue
            min_char = min(min_char, ord(char) - ord('a'))
        
        if min_char == 26:
            return 0
        
        num_operations = 26 - min_char

        return num_operations if min_char else 0