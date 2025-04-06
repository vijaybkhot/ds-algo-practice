class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # # Solution using sorting
        # stones.sort()
        # n = len(stones)
        # while True:
        #     if len(stones) > 1:
        #        stone1 = stones.pop()
        #        stone2 = stones.pop()
        #        difference = abs(stone1 - stone2)
        #        if difference > 0:
        #         stones.append(difference)
        #         if len(stones) > 1:
        #             stones.sort()
            
        #     elif len(stones) <= 1:
        #         break
        
        # return 0 if not stones else stones[0]

        # Solution using heap Data structure
        heap = []
        for num in stones:
            heapq.heappush(heap, -num)
        
        while True:
            if len(heap) > 1:
                stone1 = -heapq.heappop(heap)
                stone2 = -heapq.heappop(heap)
                difference = abs(stone1 - stone2)
                if difference > 0:
                    heapq.heappush(heap, -difference)

            elif len(heap) <=1:
                break
        return 0 if not heap else -heap[0]
        

        