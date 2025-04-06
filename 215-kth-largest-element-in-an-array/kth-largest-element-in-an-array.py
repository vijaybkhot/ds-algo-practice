class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # Solution using built in heap data structure
        # heap = []
        # for num in nums:
        #     if len(heap) < k:
        #         heapq.heappush(heap, num)
        #     else:
        #         heapq.heappushpop(heap, num)
        # return heap[0]
        # Solution using custom heap
        def heappush(heap, val):
            heap.append(val)
            bubble_up(heap, len(heap)-1)
            

        def bubble_up(heap, idx):
            while idx > 0:
                parent_idx = (idx - 1) // 2
                if heap[parent_idx] <= heap[idx]:
                    break
                heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
                idx = parent_idx

        def remove_min(heap):
            if len(heap) == 1:
                return heap.pop()
            elif len(heap) == 0:
                return None
            root, last = heap[0], heap[-1]
            heap.pop()
            heap[0] = last
            bubble_down(heap, 0)
            return root
        
        def bubble_down(heap, idx):
            n = len(heap)
            while True:
                left = (2 * idx) + 1
                right = (2*idx) + 2
                smallest = idx
                if left < n and heap[left] < heap[smallest]:
                    smallest = left
                if right < n and heap[right] < heap[smallest]:
                    smallest = right
                if idx == smallest:
                    break
                heap[smallest], heap[idx] = heap[idx], heap[smallest]
                idx = smallest
        
        heap = []

        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                remove_min(heap)
        
        return heap[0]
            

            
            

