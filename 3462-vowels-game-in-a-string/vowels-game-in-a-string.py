class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in "aeiou" for c in s)
        
        vowel_count = 0

        for char in s:
            if char in "aeiou":
                vowel_count += 1
        
        if vowel_count == 0:
            return False
        if vowel_count == 1:
            return True
        return vowel_count % 2 == 0