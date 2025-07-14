class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l, r  = len(a)-1, len(b)-1
        carry = 0
        res_str = ""
        while l >=0 or r >= 0:
            num1 = int(a[l]) if l >= 0 else 0
            num2 = int(b[r]) if r >= 0 else 0
            curr_sum = num1 + num2 + carry
            if curr_sum == 0:
                res_str = '0' + res_str
                carry = 0
            elif curr_sum == 1:
                res_str = '1' + res_str
                carry = 0
            elif curr_sum == 2:
                res_str = '0' + res_str
                carry = 1
            elif curr_sum == 3:
                res_str = '1' + res_str
                carry = 1
            
            l -= 1
            r -= 1
        
        if carry:
            res_str = '1'+res_str
        
        return res_str
        
                
        