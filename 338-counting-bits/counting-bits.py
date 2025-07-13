class Solution:
    def countBits(self, n: int) -> List[int]:

        # def binary(num):
        #     if num == 0:
        #         return [0]
        #     remainder = []
        #     while num > 0:
        #         remainder.append(num % 2)
        #         num = num // 2
        #     return remainder[::-1]

        # res = []
        # for i in range(n+1):
        #     res.append(binary(i).count(1))
        
        # return res
        res = []
        for i in range(n+1):
            count = 0
            x = i  # ✅ temp copy to preserve `i`
            while x != 0:
                x = x & (x - 1)
                count += 1
            res.append(count)
        
        return res
            



        