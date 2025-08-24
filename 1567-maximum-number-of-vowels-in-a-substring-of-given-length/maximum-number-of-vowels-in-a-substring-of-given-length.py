class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        # initial window vowel count
        vowel_count = sum(1 for c in s[:k] if c in vowels)
        res = vowel_count
        
        left = 0
        for right in range(k, len(s)):
            # remove left char
            if s[left] in vowels:
                vowel_count -= 1
            # add right char
            if s[right] in vowels:
                vowel_count += 1
            res = max(res, vowel_count)
            left += 1
        
        return res