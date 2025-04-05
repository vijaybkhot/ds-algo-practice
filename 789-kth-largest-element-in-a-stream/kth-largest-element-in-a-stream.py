class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self._insert(num)
        
        

    def add(self, val: int) -> int:
        self._insert(val)
        return self.heap[0]
    
    def _insert(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap)-1)
        if len(self.heap) > self.k:
            self._remove_min()
    
    def _bubble_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent] <= self.heap[idx]:
                break
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
    
    def _remove_min(self):
        last = self.heap.pop()
        if not self.heap:
            return
        self.heap[0] = last
        self._bubble_down(0)

    def _bubble_down(self, idx):
        n = len(self.heap)
        while True:
            smallest = idx
            left = (idx * 2) + 1
            right = (idx * 2) + 2
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if idx == smallest:
                break
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            idx = smallest



        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)