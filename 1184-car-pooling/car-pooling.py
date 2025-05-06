class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # # Function to add current trip to the heap
        # def addToHeap(heap, current_trip, curr_capacity, to, cap):
        #     heapq.heappush(heap, (to, cap))
        #     current_trip += 1
        #     curr_capacity += cap
        #     return current_trip, curr_capacity

        # curr_capacity = 0
        # organized_trips = [(trip[1], trip[2],trip[0]) for trip in trips]
        # organized_trips.sort(key=lambda x: x[0])
        
        # current_trip = 0
        # last_trip = len(trips)
        # heap = []

        # while current_trip < last_trip:
        #     curr_frm, curr_dest, curr_cap = organized_trips[current_trip]
        #     if heap and curr_frm >= heap[0][0]:
        #         while heap and curr_frm >= heap[0][0]:
        #             curr_capacity -= heap[0][1]
        #             heapq.heappop(heap)
        #     current_trip, curr_capacity = addToHeap(heap, current_trip, curr_capacity, curr_dest, curr_cap)
        #     if curr_capacity > capacity:
        #         return False
            
        # return True

        # curr_capacity = 0
        # organized_trips = [(trip[1], trip[2],trip[0]) for trip in trips]
        # organized_trips.sort(key=lambda x: x[0])

        # current_trip = 0
        # last_trip = len(trips)
        # heap = []

        # while current_trip < last_trip:
        #     curr_start, curr_end, num_passengers = organized_trips[current_trip]
        #     heapq.heappush(heap, (curr_end, num_passengers, curr_start))
        #     curr_capacity += num_passengers
        #     while heap and heap[0][0] <= curr_start:
        #         _, passengers, _ = heapq.heappop(heap)
        #         curr_capacity -= passengers

        #     if curr_capacity >  capacity:
        #         return False
        #     current_trip += 1
        
        # return True

        capacity_arr = [0] * 1001
        trips.sort(key=lambda x: x[1])

        for num_passengers, src, dst in trips:
            for i in range(src, dst):
                capacity_arr[i] += num_passengers
                if capacity_arr[i] > capacity:
                    return False
        return True












