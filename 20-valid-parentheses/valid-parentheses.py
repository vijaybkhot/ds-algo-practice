class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if stack and ((s[i] == ")" and stack[-1] == "(") or (s[i] == "}" and stack[-1] == "{") or (s[i] == "]" and stack[-1] == "[")):
                    stack.pop()
                else:
                    return False
                
        return not stack
        