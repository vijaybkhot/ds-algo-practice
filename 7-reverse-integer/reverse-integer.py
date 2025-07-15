class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        x = abs(x)
        reverse = int(str(x)[::-1])
        if temp < 0:
            reverse *= -1
        
        if reverse < -(1 << 31) or reverse > (1 << 31)-1:
            return 0
        
        return reverse
        