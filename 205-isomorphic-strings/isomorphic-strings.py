class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_t_map = dict()
        t_s_map = dict()
        
        for idx, char in enumerate(s):
            t_char = t[idx]
            if char not in s_t_map and t[idx] not in t_s_map:
                s_t_map[char] = t[idx]
                t_s_map[t[idx]] = char
            else:
                if char not in s_t_map or t_char not in t_s_map or s_t_map[char] != t_char or t_s_map[t_char] != char:
                    return False

        return True