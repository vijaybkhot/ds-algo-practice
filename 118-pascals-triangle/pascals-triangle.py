class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            prev = res[-1]
            curr = [1]
            for i in range(1, len(prev)):
                curr.append(prev[i]+prev[i-1])
            curr.append(1)
            res.append(curr)
        
        return res
