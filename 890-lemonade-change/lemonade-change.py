class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        i = 0
        while i < len(bills):
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10:
                if five:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
                    
            i += 1
        
        return True
        