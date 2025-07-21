class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        
        # while i < len(s):
        #     curr_char = s[i]
        #     count = 0
        #     while i < len(s) and s[i] == curr_char:
        #         count += 1
        #         i += 1
        #     count = min(count, 2)
        #     res += (curr_char * count)
        prev = s[0]
        count = 1
        res = s[0]
        for i in range(1, len(s)):
            if s[i] == prev:
                if count < 2:
                    count += 1
                    res += s[i]
                else:
                    continue
            else:
                prev = s[i]
                count = 1
                res += s[i]
                    
        return res