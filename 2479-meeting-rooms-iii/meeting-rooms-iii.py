class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        available_rooms = list(range(n))  # room indices
        heapq.heapify(available_rooms)
        
        ongoing_meetings = []  # (end_time, room_idx)
        room_usage = [0] * n
        
        for start, end in meetings:
            # Free up rooms
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                _, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, room)
            
            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
                room_usage[room] += 1
            else:
                # Wait until the next room is free
                next_end, room = heapq.heappop(ongoing_meetings)
                duration = end - start
                new_end = next_end + duration
                heapq.heappush(ongoing_meetings, (new_end, room))
                room_usage[room] += 1
        
        # Return the room with max meetings, break ties by room number
        max_meetings = max(room_usage)
        for i in range(n):
            if room_usage[i] == max_meetings:
                return i