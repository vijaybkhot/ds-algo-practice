class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        res = []
        while i < len(s):
            curr_char = s[i]
            count = 0
            while i < len(s) and s[i] == curr_char:
                count += 1
                i += 1
            count = min(count, 2)
            res.append(curr_char * count)
        
        return ''.join(res)