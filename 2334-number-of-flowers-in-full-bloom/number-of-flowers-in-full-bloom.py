class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        indexed_people = [(time, idx) for idx, time in enumerate(people)]
        indexed_people.sort()
        i = 0
        heap = []
        res = [0]*len(people)
        for time, idx in indexed_people:
            
            while i < len(flowers) and flowers[i][0] <= time:
                start, end = flowers[i]
                heapq.heappush(heap, (end))
                i += 1
            while heap and heap[0] < time:
                heapq.heappop(heap)
            
            res[idx] = len(heap)
        
        return res
            



        