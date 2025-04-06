class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        
        n = len(stones)
        while True:
            if len(stones) > 1:
               stone1 = stones.pop()
               stone2 = stones.pop()
               difference = abs(stone1 - stone2)
               if difference > 0:
                stones.append(difference)
                if len(stones) > 1:
                    stones.sort()
            
            elif len(stones) <= 1:
                break
        
        return 0 if not stones else stones[0]
            
        

        