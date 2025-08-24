class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
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
        res = count_vowels(counter)
        left = 0
        while right < len(s):
            counter[s[left]] -= 1
            if counter[s[left]] == 0:
                del counter[s[left]]
            counter[s[right]] += 1
            left += 1
            right += 1
            res = max(res, count_vowels(counter))
        
        return res


