class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_map = Counter()

        left = 0
        res = 0

        for right in range(len(s)):
            curr_map[s[right]] += 1
            while left <= right and curr_map[s[right]] > 1:
                curr_map[s[left]] -= 1
                if curr_map[s[left]] == 0:
                    del curr_map[s[left]]
                left += 1

            res = max(res, len(curr_map))
        
        return res
