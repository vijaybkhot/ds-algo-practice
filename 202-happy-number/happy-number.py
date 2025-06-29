class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set()
        while True:
            new_num = 0
            str_num = str(n)
            for c in str_num:
                new_num += int(c)*int(c)
            
            if new_num == 1:
                return True
            elif new_num in num_set:
                return False
            num_set.add(new_num)
            n = new_num


        