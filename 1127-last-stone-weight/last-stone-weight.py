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

        
        # def heapify(heap):
        #     n = len(heap)
        #     for i in reversed(range(n // 2)):
        #         bubble_down(heap, i, n)
        
        # def bubble_down(heap, idx, n):
        #     while idx < n:
        #         largest = idx
        #         left = (2*idx) + 1
        #         right = (2*idx) + 2
        #         if left < n and heap[left] > heap[largest]:
        #             largest = left
        #         if right < n and heap[right] > heap[largest]:
        #             largest = right
        #         if largest == idx:
        #             break
        #         heap[largest], heap[idx] = heap[idx], heap[largest]
        #         idx = largest


        # def heappush(heap: List[int], val: int):
        #     heap.append(val)
        #     if len(heap) == 1:
        #         return heap
        #     child = len(heap) - 1
        #     while child > 0:
        #         parent = (child-1) // 2
        #         if heap[parent] >= heap[child]:
        #             break
        #         heap[child], heap[parent] = heap[parent], heap[child]
        #         child = parent
        #     return heap
        
        # def heappop(heap):
        #     if len(heap) == 1:
        #         return heap.pop()
        #     elif len(heap) == 0:
        #         return None
        #     heap[0], heap[-1] = heap[-1], heap[0]
        #     root = heap.pop()
        #     # Bubble down
        #     child = 0
        #     n = len(heap)
        #     while child < n:
        #         left = (2*child) + 1
        #         right = (2*child + 2)
        #         largest = child
        #         if left < n and heap[left] > heap[largest]:
        #             largest = left
                
        #         if right < n and heap[right] > heap[largest]:
        #             largest = right
                
        #         if largest == child:
        #             break
        #         heap[largest], heap[child] = heap[child], heap[largest]
        #         child = largest

        #     return root
        
        # heapify(stones)
        
        # while True:
        #     if len(stones) > 1:
        #         stone1 = heappop(stones)
        #         stone2 = heappop(stones)
        #         difference = abs(stone1 - stone2)
        #         if difference > 0:
        #             heappush(stones, difference)
        #     elif len(stones) <= 1:
        #         break
        # return 0 if not stones else stones[0]


        # stones_max = [-stone for stone in stones]
        # heapq.heapify(stones_max)
        # n = len(stones_max)
        # remaining = n
        # while remaining >= 2:
        #     if len(stones_max) >= 2:
        #         stone1 = -heapq.heappop(stones_max)
        #         stone2 = -heapq.heappop(stones_max)
        #         if stone1 > stone2:
        #             new_stone = stone1 - stone2
        #             heapq.heappush(stones_max, -new_stone)
        #             remaining -= 1
        #         else:
        #             remaining -= 2


        
        # return -stones_max[0] if stones_max else 0

        def heapify(heap):
            last_non_leaf = (len(heap)-1)//2
            for i in range(last_non_leaf, -1, -1):
                bubble_down(heap, i)
            return heap

        def insert(heap, val):
            heap.append(val)
            bubble_up(heap, len(heap)-1)
            return heap

        def bubble_up(heap, idx):
            while idx > 0:
                parent_idx = (idx-1) // 2
                if heap[parent_idx] >= heap[idx]:
                    break
                heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
                idx = parent_idx
            return heap
        
        def max_pop(heap):
            heap[0], heap[-1] = heap[-1], heap[0]
            max_val = heap.pop()
            heap = bubble_down(heap, 0)
            return heap, max_val
        
        def bubble_down(heap, idx):
            while idx < len(heap):
                largest = idx
                left = (2 * idx) + 1
                right = (2 * idx) + 2
                if left < len(heap) and heap[left] > heap[largest]:
                    largest = left
                if right < len(heap) and heap[right] > heap[largest]:
                    largest = right
                if largest == idx:
                    break
                heap[largest], heap[idx] = heap[idx], heap[largest]
                idx = largest
            return heap

        max_heap = heapify(stones)

        while len(max_heap) > 1:
            if len(max_heap) > 1:
                max_heap, stone1 = max_pop(max_heap)
                max_heap, stone2 = max_pop(max_heap)
                if stone1 != stone2:
                    new_stone = stone1 - stone2
                    max_heap = insert(max_heap, new_stone)
        
        return max_heap[0] if max_heap else 0



            
        

        