class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_set = set(t)
        
        
        t_map = Counter(t)

        res = ""
        len_res = float('inf')
        left = 0
        curr_map = Counter()
        for right in range(len(s)):
            curr_char = s[right]
            if curr_char in t_set:
                curr_map[curr_char] += 1
            while all(curr_map[c] >= t_map[c] for c in t_map) and left <= right:
                if (right - left + 1) < len_res:
                    res = s[left:right+1]
                    len_res = right - left + 1

                left_char = s[left]
                if left_char in curr_map:
                    curr_map[left_char] -= 1
                left += 1
        
        return res
