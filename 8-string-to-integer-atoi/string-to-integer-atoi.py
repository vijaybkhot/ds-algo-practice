class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = -1*(2**31)
        MAX = (2**31)-1

        s = s.strip()
        i = 0
        if i < len(s)  and s[i] not in "+-0123456789":
            return 0
        sign = "+"
        if i < len(s) and s[i] in "+-":
            sign = "-" if s[i]=="-" else "+"
            i += 1
        
        res = 0
        exceeded = False
        while i < len(s) and s[i] in "0123456789":
            res = res*10+int(s[i])
            if res > MAX:
                res = MAX
                exceeded = True
                break
            i += 1
        
        if sign == '-':
            res = (res*-1)
        
        if res == -MAX and exceeded:
            res = MIN
        
        return res
