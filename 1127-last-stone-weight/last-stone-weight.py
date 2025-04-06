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
        # heap = []
        # for num in stones:
        #     heapq.heappush(heap, -num)
        
        # while True:
        #     if len(heap) > 1:
        #         stone1 = -heapq.heappop(heap)
        #         stone2 = -heapq.heappop(heap)
        #         difference = abs(stone1 - stone2)
        #         if difference > 0:
        #             heapq.heappush(heap, -difference)

        #     elif len(heap) <=1:
        #         break
        # return 0 if not heap else -heap[0]

        
        def heapify(heap):
            n = len(heap)
            for i in reversed(range(n // 2)):
                bubble_down(heap, i, n)
        
        def bubble_down(heap, idx, n):
            while idx < n:
                largest = idx
                left = (2*idx) + 1
                right = (2*idx) + 2
                if left < n and heap[left] > heap[largest]:
                    largest = left
                if right < n and heap[right] > heap[largest]:
                    largest = right
                if largest == idx:
                    break
                heap[largest], heap[idx] = heap[idx], heap[largest]
                idx = largest
            

            

        def heappush(heap: List[int], val: int):
            heap.append(val)
            if len(heap) == 1:
                return heap
            child = len(heap) - 1
            while child > 0:
                parent = (child-1) // 2
                if heap[parent] >= heap[child]:
                    break
                heap[child], heap[parent] = heap[parent], heap[child]
                child = parent
            return heap
        
        def heappop(heap):
            if len(heap) == 1:
                return heap.pop()
            elif len(heap) == 0:
                return None
            heap[0], heap[-1] = heap[-1], heap[0]
            root = heap.pop()
            # Bubble down
            child = 0
            n = len(heap)
            while child < n:
                left = (2*child) + 1
                right = (2*child + 2)
                largest = child
                if left < n and heap[left] > heap[largest]:
                    largest = left
                
                if right < n and heap[right] > heap[largest]:
                    largest = right
                
                if largest == child:
                    break
                heap[largest], heap[child] = heap[child], heap[largest]
                child = largest

            return root
        
        heapify(stones)
        
        while True:
            if len(stones) > 1:
                stone1 = heappop(stones)
                stone2 = heappop(stones)
                difference = abs(stone1 - stone2)
                if difference > 0:
                    heappush(stones, difference)
            elif len(stones) <= 1:
                break
        return 0 if not stones else stones[0]



            
        

        