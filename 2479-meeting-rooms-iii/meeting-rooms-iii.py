class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        # # First attempt - Partially Correct:
        # heapq.heapify(meetings)
        # meeting_rooms = [(-1, i, 0) for i in range(n)] # meeting end time, idx, num meetings
        # heapq.heapify(meeting_rooms)
        # curr_time = 0
        # while meetings:
        #     while meeting_rooms[0][0] >= 0 and meeting_rooms[0][0] <= curr_time:
        #         curr_end, idx, num_meetings  = heapq.heappop(meeting_rooms)
        #         heapq.heappush(meeting_rooms, (-1, idx, num_meetings))

        #     if meeting_rooms[0][0] < 0:
        #         curr_time = max(curr_time, meetings[0][0])
        #         start, end = heapq.heappop(meetings)
        #         curr_end, idx, num_meetings = heapq.heappop(meeting_rooms)
        #         heapq.heappush(meeting_rooms, (curr_time+end-start, idx, num_meetings+1))
        #     else:
        #         curr_end, idx, num_meetings  = heapq.heappop(meeting_rooms)
        #         curr_time = max(curr_time, curr_end)
        #         heapq.heappush(meeting_rooms, (-1, idx, num_meetings))

        
        # for i, (curr_end, idx, num_meetings) in enumerate(meeting_rooms):
        #     meeting_rooms[i] = (-1, -num_meetings, idx)

        # heapq.heapify(meeting_rooms)
        
        # return meeting_rooms[0][2]

        # Improved approach

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

                

                

           