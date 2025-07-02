class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            heapq.heappush(heap, (abs(x-num), num))
        
        res = []
        for i in range(k):
            _, num = heapq.heappop(heap)
            res.append(num)
        res.sort()
        return res