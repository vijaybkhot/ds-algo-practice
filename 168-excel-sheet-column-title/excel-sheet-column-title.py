class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if columnNumber == 0:
            return ""

        n = columnNumber - 1
        return self.convertToTitle(n//26) + chars[n%26]

        # res = ""
        # while columnNumber > 0:
        #     offset = (columnNumber - 1) % 26
        #     res += chars[offset]
        #     columnNumber= (columnNumber-1)//26

        # return res[::-1]
