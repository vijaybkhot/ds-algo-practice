from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):
            return res

        # frequency arrays for p and sliding window
        p_count = [0] * 26
        s_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        left = 0
        for right in range(len(s)):
            s_count[ord(s[right]) - ord('a')] += 1

            # shrink window if it's bigger than p
            if right - left + 1 > len(p):
                s_count[ord(s[left]) - ord('a')] -= 1
                left += 1

            # check if current window matches
            if s_count == p_count:
                res.append(left)

        return res
