class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_capacity = 0
        organized_trips = [(trip[1], trip[2],trip[0]) for trip in trips]
        organized_trips.sort(key=lambda x: x[0])
        
        current_trip = 0
        last_trip = len(trips)
        heap = []

        def addToHeap(heap, current_trip, curr_capacity, to, cap):
            heapq.heappush(heap, (to, cap))
            current_trip += 1
            curr_capacity += cap
            return current_trip, curr_capacity

        

        while current_trip < last_trip:
            if current_trip < last_trip and not heap:
                frm, to, cap = organized_trips[current_trip]
                current_trip, curr_capacity = addToHeap(heap, current_trip, curr_capacity, to, cap)
                if curr_capacity > capacity:
                    return False
                continue
               
            curr_frm, curr_dest, curr_cap = organized_trips[current_trip]
            if curr_frm >= heap[0][0]:
                while heap and curr_frm >= heap[0][0]:
                    curr_capacity -= heap[0][1]
                    heapq.heappop(heap)
                current_trip, curr_capacity = addToHeap(heap, current_trip, curr_capacity, curr_dest, curr_cap)
                if curr_capacity > capacity:
                    return False
            elif curr_frm < heap[0][0]:
                current_trip, curr_capacity = addToHeap(heap, current_trip, curr_capacity, curr_dest, curr_cap)
                if curr_capacity > capacity:
                    return False

        return True            