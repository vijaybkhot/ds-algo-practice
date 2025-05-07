class MedianFinder:

    # def __init__(self):
        

    # def addNum(self, num: int) -> None:
        

    # def findMedian(self) -> float:

    #Approach using insert in order - Less Efficient. The addSum Operation take O(n) time
    # def __init__(self):
    #     self.arr = []
        
    # def addNum(self, num: int) -> None:
    #     self.arr.append(num)
    #     # Reorder
    #     i = len(self.arr) - 1
    #     while i > 0 and self.arr[i] < self.arr[i - 1]:
    #         self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]
    #         i -= 1
        
    # def findMedian(self) -> float:
    #     n = len(self.arr)
    #     if n % 2:
    #         return self.arr[n//2]
    #     else:
    #         return (self.arr[n//2] + self.arr[(n//2) - 1]) / 2

    # # Solution using two heaps - More Efficient
    # def __init__(self):
    #     self.min_heap = []  # Large Elements  
    #     self.max_heap = []  # Small elements

    # def addNum(self, num: int) -> None:
    #     # Push the new num to the max_heap, i.e. heap with small elements
    #     heapq.heappush(self.max_heap, -num)
    #     # Push the largest element in max_heap to the min_heap
    #     heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    #     # If there is imbalance, balance the heaps by moving the smallest element from min_heap to max_heap
    #     if len(self.min_heap) > len(self.max_heap):
    #         heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    # def findMedian(self) -> float:
    #     if len(self.max_heap) == len(self.min_heap):
    #         return (-self.max_heap[0] + self.min_heap[0]) / 2
    #     else:
    #         return -self.max_heap[0]

    # def __init__(self):
    #     self.large = [] # Min heap
    #     self.small = [] # Max heap
        

    # def addNum(self, num: int) -> None:
    #     # Add a larger number to the heap containing large numbers
    #     if self.large and num > self.large[0]:
    #         heapq.heappush(self.large, num)
    #     # Else add to the heap containing smaller numbers
    #     else:
    #         heapq.heappush(self.small, -num)

    #     # balance the heaps if any one heap's length is larger than 1 than the length of the other 
    #     if len(self.large) > len(self.small) + 1:
    #         val = heapq.heappop(self.large)
    #         heapq.heappush(self.small, -val)
        
    #     if len(self.small) > len(self.large) + 1:
    #         val = -1 * heapq.heappop(self.small)
    #         heapq.heappush(self.large, val) 

    # def findMedian(self) -> float:
    #     # Return the root of the heap having more elements
    #     if len(self.large) > len(self.small):
    #         return self.large[0]
    #     elif len(self.small) > len(self.large):
    #         return -self.small[0]
    #     # Return the avergae of the two roots if both heaps have the same number of elements
    #     else:
    #         return (-self.small[0] + self.large[0]) / 2.0

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        len_min, len_max = len(self.min_heap), len(self.max_heap)
        if len_min - len_max > 1:
            element = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -element)
        
        if len_max - len_min > 1:
            element = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -element)
    
        
    def findMedian(self) -> float:
        len_min, len_max = len(self.min_heap), len(self.max_heap)
        if len_min > len_max:
            return self.min_heap[0]
        elif len_min < len_max:
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0])/2

        
         
    # def __init__(self):
        

    # def addNum(self, num: int) -> None:
       
        
        

    # def findMedian(self) -> float:

        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()