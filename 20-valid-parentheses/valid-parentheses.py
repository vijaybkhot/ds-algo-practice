class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for bracket in s:
            if bracket in ['(', '{', '[']:
                stack.append(bracket)
            else:
                if bracket == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif bracket == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif bracket == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        if stack:
            return False

        return True