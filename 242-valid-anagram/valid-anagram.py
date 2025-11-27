class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = [char for char in s]
        s_arr.sort()
        t_arr = [char for char in t]
        t_arr.sort()
        return ''.join(s_arr) == ''.join(t_arr)