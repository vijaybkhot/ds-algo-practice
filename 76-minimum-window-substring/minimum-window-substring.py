class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if not s or not t:
            return ""
        
        t_map = Counter(t)
        s_map = Counter()
        required = len(t_map)
        have = 0

        left = 0
        res = [-1, -1]
        len_res = float('inf')

        for right in range(len(s)):
            char = s[right]
            if char in t_map:
                s_map[char] += 1
                if s_map[char] == t_map[char]:
                    have += 1
            
            while have == required:
                if right-left+1 < len_res:
                    len_res = right-left+1
                    res = [left,right]
                left_char = s[left]
                if left_char in s_map:
                    s_map[left_char] -= 1
                    if s_map[left_char] < t_map[left_char]:
                        have -= 1
                left += 1
        
        l, r = res
        return s[l:r+1] if len_res != float('inf') else ""
