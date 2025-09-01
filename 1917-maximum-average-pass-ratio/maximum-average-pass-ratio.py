class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        # [[1,2],[3,5],[2,2]]
        # heap: []

        average_heap = [(-((p+1)/(t+1) - p/t), p, t) for p, t in classes]

        heapq.heapify(average_heap)
        print(average_heap)
        while extraStudents:
            _, curr_p, curr_t = heapq.heappop(average_heap)
            new_p, new_t = curr_p+1, curr_t+1
            new_expected_increase = ((new_p+1)/(new_t+1)) - (new_p/new_t)
            heapq.heappush(average_heap, (-new_expected_increase, new_p, new_t))
            extraStudents -= 1
        res = 0
        for _, p, t in average_heap:
            res += p/t
        
        return res/len(classes)


