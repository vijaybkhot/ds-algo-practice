class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        count = 1
        num = n - 1

        while '0' in (str(num)) or '0' in (str(count)):
            count += 1
            num -= 1
        
        return [count, num]
