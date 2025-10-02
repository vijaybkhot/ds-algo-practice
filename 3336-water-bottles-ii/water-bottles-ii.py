class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = 0
        empty = 0
        
        while numBottles+empty >= numExchange:
            
            while empty >= numExchange:
                numBottles += 1
                empty -= numExchange
                numExchange += 1
            drunk += numBottles 
            empty += numBottles 
            numBottles = 0
        
        return drunk+numBottles