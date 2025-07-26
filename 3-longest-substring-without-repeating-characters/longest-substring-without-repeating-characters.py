class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        res = 0
        left = 0
        for right in range(len(s)):
            while left <= right and s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, len(char_set))
        
        return res