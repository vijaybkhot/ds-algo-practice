class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = -2**31
        MAX = 2**31 - 1

        s = s.strip()
        if not s:
            return 0

        i = 0
        sign = 1

        if s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1

        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        res *= sign
        return max(MIN, min(MAX, res))
