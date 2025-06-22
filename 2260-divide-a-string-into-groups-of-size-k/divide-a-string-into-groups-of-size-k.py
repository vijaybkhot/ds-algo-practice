class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        for i in range(0, len(s), k):
            curr_str = ""
            for j in range(k):
                if i+j < len(s):
                    curr_str += s[i+j]
                else:
                    curr_str += fill

            res.append(curr_str)
        
        return res

        