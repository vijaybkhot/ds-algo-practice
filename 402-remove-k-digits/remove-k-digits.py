class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:
            c = int(char)
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            if not stack and c == 0:
                continue
            stack.append(c)
        while k and stack:
            stack.pop()
            k -= 1
        if not stack:
            stack.append(0)
        str_num = ''.join([str(char) for char in stack])
        return str_num