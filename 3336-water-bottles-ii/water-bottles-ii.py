class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = 0
        empty = 0
        #        2                   8
        while numBottles+empty >= numExchange:
            #       0      8
            while empty >= numExchange:
                numBottles += 1
                empty -= numExchange
                numExchange += 1
            drunk += numBottles #15
            empty += numBottles # 13
            numBottles = 0
        
        return drunk+numBottles