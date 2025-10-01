class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # bott = 3, exc = 4
        drink = 0   # 15+3,
    
        empty = 0   # 2
        new_num_bottles = 0 #1
        while (numBottles+empty) >= numExchange:
            drink += numBottles
            new_num_bottles = (numBottles+empty) // numExchange
            empty = (numBottles+empty)%numExchange
            numBottles = new_num_bottles
        
        return drink+numBottles