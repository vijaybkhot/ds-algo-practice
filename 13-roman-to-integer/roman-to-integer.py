class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = 0

        dict_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        while i < len(s):
            curr_num = dict_map[s[i]]
            i += 1

            if i < len(s) and dict_map[s[i]] > curr_num:
                num -= curr_num
            else:
                num += curr_num
        
        return num
