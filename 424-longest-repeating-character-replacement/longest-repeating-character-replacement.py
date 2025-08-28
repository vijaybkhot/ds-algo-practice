class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter(s)
        res = 0
        for char in counter:
            left = 0
            non_char = 0
            for right in range(len(s)):
                if s[right] != char:
                    non_char += 1
                
                while left <= right and non_char > k:
                    if s[left] != char:
                        non_char -= 1
                    left += 1
                res = max(res, right-left+1)
        
        return res