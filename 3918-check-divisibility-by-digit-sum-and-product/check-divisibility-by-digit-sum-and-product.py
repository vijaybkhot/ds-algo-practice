class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_digits, prod_digits = 0, 1
        num_str = str(n)
        for num in num_str:
            curr_num = int(num)
            sum_digits += curr_num
            prod_digits *= curr_num
        
        return not (n % (sum_digits+prod_digits))