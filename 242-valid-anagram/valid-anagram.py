class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_arr = [char for char in s]
        # s_arr.sort()
        # t_arr = [char for char in t]
        # t_arr.sort()
        # return ''.join(s_arr) == ''.join(t_arr)
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        for char in s:
            s_map[char] += 1
        for char in t:
            t_map[char] += 1
        
        for char in s_map:
            if s_map[char] != t_map[char]:
                return False
        
        for char in t_map:
            if s_map[char] != t_map[char]:
                return False
        
        return True