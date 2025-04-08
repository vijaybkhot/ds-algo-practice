class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_capacity = 0
        organized_trips = [(trip[1], trip[2],trip[0]) for trip in trips]
        organized_trips.sort(key=lambda x: x[0])
        max_distance = trips[0][1]
        for trip in organized_trips:
            max_distance = max(max_distance, trip[1])
        
        start, destination = trips[0][0], max_distance
        current_trip = 0
        n = len(trips)
        heap = []


        while current_trip < n:
            if current_trip < n and not heap:
                frm, to, cap = organized_trips[current_trip]
                heapq.heappush(heap, (to, cap))
                current_trip += 1
                curr_capacity += cap
                if curr_capacity > capacity:
                    return False
                if current_trip >= n:
                    break
            curr_frm, curr_dest, curr_cap = organized_trips[current_trip]
            if curr_frm >= heap[0][0]:
                while heap and curr_frm >= heap[0][0]:
                    curr_capacity -= heap[0][1]
                    heapq.heappop(heap)
                heapq.heappush(heap, (curr_dest, curr_cap))
                current_trip += 1
                curr_capacity += curr_cap
                if curr_capacity > capacity:
                    return False
                if current_trip >= n:
                    break
            elif curr_frm < heap[0][0]:
                heapq.heappush(heap, (curr_dest, curr_cap))
                current_trip += 1
                curr_capacity += curr_cap
                if curr_capacity > capacity:
                    return False
                if current_trip >= n:
                    break

        return True
            
            
                

        return True
            