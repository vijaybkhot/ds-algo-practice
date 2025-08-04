class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for paren in s:
            if paren in "([{":
                stack.append(paren)
            else:
                if paren == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if paren == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                
                if paren == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False   
        return not stack