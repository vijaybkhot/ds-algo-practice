class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = defaultdict(str)
        i = 0
        curr_row = 0
        down = True
        while i < len(s):
            while i < len(s) and curr_row < numRows:
                rows[curr_row] += s[i]
                curr_row += 1
                i += 1
            curr_row = numRows - 2
            while i < len(s) and curr_row > 0:
                rows[curr_row] += s[i]
                curr_row -= 1
                i += 1
        res = ""
        for i in range(numRows):
            res += rows[i]

        return res
