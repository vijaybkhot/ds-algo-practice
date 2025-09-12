class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        vowel_count = 0

        for char in s:
            if char in "aeiou":
                vowel_count += 1
        
        if vowel_count == 0:
            return False
        return True