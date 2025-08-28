class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        char_map = Counter()

        max_len = 0

        for right in range(len(s)):
            char_map[s[right]] += 1

            while left <= right and char_map[s[right]] > 2:
                char_map[s[left]] -= 1
                left += 1
            
            max_len = max(max_len,right - left + 1)
        
        return max_len