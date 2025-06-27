class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        res = ""

        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            res += chars[offset]
            columnNumber= (columnNumber-1)//26

        return res[::-1]
