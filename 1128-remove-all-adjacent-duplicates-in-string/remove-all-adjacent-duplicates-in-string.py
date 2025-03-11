class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
                continue
            else:
                stack.append(char)
        
        return "".join(stack)
            