class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # # Initial attempt
        # # Implement a priority queue to maintain a queue of length k
        # def enque(q, point):
        #     q.append(point)
        #     bubble_up(q)
        #     if len(q) > k:
        #         remove_max(q)

        # def bubble_up(q):
        #     idx = len(q) - 1
        #     while idx > 0:
        #         parent_idx = (idx-1) // 2
        #         child = (q[idx][0]**2 + q[idx][1]**2) ** (1/2) 
        #         parent = (q[parent_idx][0]**2 + q[parent_idx][1]**2) ** (1/2)
        #         if parent >= child:
        #             break
        #         q[idx], q[parent_idx] = q[parent_idx], q[idx]
        #         idx = parent_idx  
            
        # def remove_max(q):
        #     if len(q) == 1:
        #         return q.pop()
        #     if not q:
        #         return None
        #     q[0], q[-1] = q[-1], q[0]
        #     root = q.pop()
        #     bubble_down(q)
        
        # def bubble_down(q):
        #     n = len(q)
        #     idx = 0
        #     while idx < n:
        #         left_idx = (2*idx) + 1
        #         right_idx = (2*idx) + 2
        #         child = [(q[idx][0]**2 + q[idx][1]**2) ** (1/2), idx]
        #         left = [(q[left_idx][0]**2 + q[left_idx][1]**2) ** (1/2) if left_idx < n else float('-inf'), left_idx]
        #         right = [(q[right_idx][0]**2 + q[right_idx][1]**2) ** (1/2) if right_idx < n else float('-inf'), right_idx]
        #         largest = child
        #         if left[0] > largest[0]:
        #             largest = left
        #         if right[0] > largest[0]:
        #             largest = right
        #         if child[0] == largest[0]:
        #             break
        #         q[largest[1]], q[child[1]] = q[child[1]], q[largest[1]]
        #         idx = largest[1]
            
        # queue = []
        # for point in points:
        #     enque(queue, point)
                
        # return queue

        # # Optimized attempt
        # # Implement a priority queue to maintain a queue of length k
        # def enque(q, point):
        #     q.append(point)
        #     bubble_up(q)
        #     if len(q) > k:
        #         remove_max(q)

        # def bubble_up(q):
        #     idx = len(q) - 1
        #     while idx > 0:
        #         parent_idx = (idx-1) // 2
        #         child = (q[idx][0]**2 + q[idx][1]**2)
        #         parent = (q[parent_idx][0]**2 + q[parent_idx][1]**2)
        #         if parent >= child:
        #             break
        #         q[idx], q[parent_idx] = q[parent_idx], q[idx]
        #         idx = parent_idx  
            
        # def remove_max(q):
        #     if len(q) == 1:
        #         return q.pop()
        #     if not q:
        #         return None
        #     q[0], q[-1] = q[-1], q[0]
        #     root = q.pop()
        #     bubble_down(q)
        
        # def bubble_down(q):
        #     n = len(q)
        #     idx = 0
        #     while idx < n:
        #         left_idx = (2*idx) + 1
        #         right_idx = (2*idx) + 2
        #         child = [(q[idx][0]**2 + q[idx][1]**2), idx]
        #         left = [(q[left_idx][0]**2 + q[left_idx][1]**2) if left_idx < n else float('-inf'), left_idx]
        #         right = [(q[right_idx][0]**2 + q[right_idx][1]**2) if right_idx < n else float('-inf'), right_idx]
        #         largest = child
        #         if left[0] > largest[0]:
        #             largest = left
        #         if right[0] > largest[0]:
        #             largest = right
        #         if child[0] == largest[0]:
        #             break
        #         q[largest[1]], q[child[1]] = q[child[1]], q[largest[1]]
        #         idx = largest[1]
            
        # queue = []
        # for point in points:
        #     enque(queue, point)
                
        # return queue

        # Using built in heap
        heap = []

        for x, y in points:
            dist = -(x**2 + y**2)
            if len(heap) < k:
                heapq.heappush(heap, (dist, [x, y]))
            else:
                heapq.heappushpop(heap, (dist, [x, y]))
                
        return [point for _, point in heap]



