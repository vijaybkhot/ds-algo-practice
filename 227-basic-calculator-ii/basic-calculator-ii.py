class Solution:
    def calculate(self, s: str) -> int:
        # n = len(s)

        # def parse_num(i):
        #     curr_num = ""
        #     while i < n and s[i].isdigit():
        #         curr_num += s[i]
        #         i += 1
        #     return curr_num, i
        
        # stack = []
        # i = 0
        # while i < len(s):
        #     if s[i] in "+-*/":
        #         stack.append(s[i])
        #         i += 1
        #     elif s[i] == ' ':
        #         i += 1
        #         continue
        #     else:
        #         curr_num, i = parse_num(i)
        #         stack.append(curr_num)
        # i = 0
        # new_stack = []
        # while i < len(stack):
        #     if stack[i] in '*/':
        #         sign = stack[i]
        #         num1 = int(new_stack.pop())
        #         i += 1
        #         num2 = int(stack[i])
        #         new_num = str(int(num1 / num2)) if sign == '/' else str(num1*num2)
        #         new_stack.append(new_num)
        #     else:
        #         new_stack.append(stack[i])
        #     i += 1
        
        # final_stack = []
        # i = 0
        # while i < len(new_stack):
        #     if new_stack[i] in '+-':
        #         sign = new_stack[i]
        #         i += 1
        #         num1 = final_stack.pop()
        #         num2 = int(new_stack[i])
        #         new_num = num1 + num2 if sign == '+' else num1-num2
        #         final_stack.append(new_num)
        #     else:
        #         final_stack.append(int(new_stack[i]))
        #     i += 1
        
        # return final_stack[0]

        # Cleaned up version
        stack = []
        sign = '+'
        num = 0

        for i, ch in enumerate(s + '+'):  # Add '+' to handle last number
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)  # Truncates toward zero
                sign = ch
                num = 0

        
        return sum(stack)
                