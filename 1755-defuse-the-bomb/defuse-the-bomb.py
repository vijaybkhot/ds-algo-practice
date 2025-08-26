class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0]*len(code)
        curr_total = sum(code[:k])
        left = 0

        # tot = 16
        #             ^
        # [12,   10,  0,  0]
        # [5,   7,  1,  4]
        if k < 0:
            curr_total = sum(code[n+k:])

            for i in range(len(code)-1, -1, -1):
                left = i
                curr_total -= code[left]
                right = (left+k)%len(code)
                curr_total += code[right]
                res[i] = curr_total
        else:
            for i in range(len(code)):
                left = i
                curr_total -= code[left]
                right = (left+k)%len(code)
                curr_total += code[right]
                res[i] = curr_total

        

        return res

