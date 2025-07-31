class Solution:
    def isHappy(self, n: int) -> bool:
        nums_set = set()
        while True:
            num = n
            new_num = 0
            while num:
                last_digit = num%10
                new_num += last_digit**2
                num = num // 10
            if new_num == 1:
                return True
            elif new_num in nums_set:
                return False
            nums_set.add(new_num)
            n = new_num