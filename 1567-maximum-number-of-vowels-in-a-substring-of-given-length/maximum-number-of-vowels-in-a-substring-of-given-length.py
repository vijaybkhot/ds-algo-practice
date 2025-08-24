class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        def count_vowels(counter):
            total = 0
            for char in counter:
                if char in "aeiou":
                    total += counter[char]
            return total
        
        counter = Counter()
        right = 0
        while right < k:
            counter[s[right]] += 1
            right += 1
        vowel_count = count_vowels(counter)
        res = vowel_count
        left = 0

        while right < len(s):
            if s[left] in vowels:
                vowel_count -= 1
            
            if s[right] in vowels:
                vowel_count += 1
           
            left += 1
            right += 1
            res = max(res, vowel_count)
        
        return res


