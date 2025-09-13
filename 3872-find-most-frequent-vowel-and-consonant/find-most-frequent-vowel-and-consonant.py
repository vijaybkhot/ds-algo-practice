class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        vowels = [char for char in s if char in "aeiou"]
        vowels_count = Counter(vowels)
        max_vowel_count = max(vowels_count.values()) if vowels_count else 0
        consonants = [char for char in s if char not in "aeiou"]
        consonant_count = Counter(consonants)
        max_consonant_count = max(consonant_count.values()) if consonant_count else 0

        return max_vowel_count+max_consonant_count