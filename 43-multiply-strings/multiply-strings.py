class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # return str(int(num1)*int(num2))
        num_map = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
         }
        def str_to_num(s):
            num = 0
            k = 10 ** (len(s)-1)
            for i in range(len(s)):
                num += k*num_map[s[i]]
                k = k//10
            return num
        
        num1 = str_to_num(num1)
        num2 = str_to_num(num2)
        # return num1
        return str(num1*num2)
        