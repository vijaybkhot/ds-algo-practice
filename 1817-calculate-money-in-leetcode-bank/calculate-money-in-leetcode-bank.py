class Solution:
    def totalMoney(self, n: int) -> int:
        
        monday = 1
        day = 0
        bank = 0
        for i in range(n):
            bank += monday + day
            day += 1

            if day == 7:
                day = 0
                monday += 1
        
        return bank
