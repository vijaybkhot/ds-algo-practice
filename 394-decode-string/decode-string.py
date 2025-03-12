class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                curr_str = ""
                while stack and stack[-1] != '[':
                    curr_str = stack.pop() + curr_str
                # Remove the opening bracket
                stack.pop()
                # Check if there is a number
                number_str = ""
                while stack and stack[-1].isdigit():
                    number_str = stack.pop() + number_str
                repeat = int(number_str)
                # Add the repeated string to stack
                stack.append(curr_str * repeat)
            else:
                stack.append(s[i])
        
        return ''.join(stack)

        