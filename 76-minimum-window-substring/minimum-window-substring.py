class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_map = Counter(t)
        curr_map = Counter()
        required_chars = len(t_map)
        res = ""
        len_res = float('inf')
        left = 0
        
        for right in range(len(s)):
            curr_char = s[right]
            curr_map[curr_char] += 1
            
            while all(curr_map[c] >= t_map[c] for c in t_map) and left <= right:
                if (right - left + 1) < len_res:
                    res = s[left:right+1]
                    len_res = right - left + 1
                
                left_char = s[left]
                curr_map[left_char] -= 1
                left += 1
        
        return res
