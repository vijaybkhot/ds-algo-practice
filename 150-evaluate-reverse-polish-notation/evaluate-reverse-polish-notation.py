class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-/*":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                print(num1, num2, token)
                if token == "+":
                    stack.append(num1+num2)
                elif token == "-":
                    stack.append(num2-num1)
                elif token == "/":
                    stack.append(int(num2/num1))
                    print(stack[-1])
                else:
                    stack.append(num1*num2)
            else:
        
                stack.append(token)
        
        return int(stack[0])