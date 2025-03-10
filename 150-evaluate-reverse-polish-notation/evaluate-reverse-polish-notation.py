class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        res = []

        for token in tokens:
            if token == '+':
                num2 = res.pop()
                num1 = res.pop()
                num3 = num1 + num2
                res.append(num3)
            elif token == '-':
                num2 = res.pop()
                num1 = res.pop()
                num3 = num1 - num2
                res.append(num3)
            elif token == '/':
                num2 = res.pop()
                num1 = res.pop()
                num3 = int(num1 / num2) if num1 * num2 > 0 else -(-num1 // num2)
                res.append(num3)
            elif token == '*':
                num2 = res.pop()
                num1 = res.pop()
                num3 = num1 * num2
                res.append(num3)
            else:
                res.append(int(token))

        return res[0]
            

        
            
            
        