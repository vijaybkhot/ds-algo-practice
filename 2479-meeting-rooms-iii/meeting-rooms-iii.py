class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        available = [i for i in range(n)]
        heapq.heapify(available)
        occupied = []
        meeting_count = [0]*n
        for start, end in meetings:
            while occupied and occupied[0][0] <= start:
                _, room_idx = heapq.heappop(occupied)
                heapq.heappush(available, room_idx)
            if available:
                room_idx = heapq.heappop(available)
                heapq.heappush(occupied, (end , room_idx))
                meeting_count[room_idx] += 1

            else:
                end_time, room_idx = heapq.heappop(occupied)
                delayed_start = end_time-start+end
                heapq.heappush(occupied, (delayed_start, room_idx))
                meeting_count[room_idx] += 1
        
        max_count = max(meeting_count)
        return meeting_count.index(max_count)


            
            


















        # meetings.sort()
        # ongoing_meetings = [] # (end_time, room_idx)
        # available_rooms = [i for i in range(n)]
        # heapq.heapify(available_rooms)
        # room_usage = [0]*n

        # for start, end in meetings:
        #     while ongoing_meetings and ongoing_meetings[0][0] <= start:
        #         end_time, room_idx = heapq.heappop(ongoing_meetings)
        #         heapq.heappush(available_rooms, room_idx)
            
        #     if available_rooms:
        #         room_idx = heapq.heappop(available_rooms)
        #         heapq.heappush(ongoing_meetings, (end, room_idx))
        #         room_usage[room_idx] += 1
        #     else:
        #         # Delayed start
        #         end_time, room_idx = heapq.heappop(ongoing_meetings)
        #         delayed_start = end_time + end - start
        #         heapq.heappush(ongoing_meetings, (delayed_start, room_idx))
        #         room_usage[room_idx] += 1
        
        # return room_usage.index(max(room_usage))
        


                


        # # # First attempt - Partially Correct:
        # # heapq.heapify(meetings)
        # # meeting_rooms = [(-1, i, 0) for i in range(n)] # meeting end time, idx, num meetings
        # # heapq.heapify(meeting_rooms)
        # # curr_time = 0
        # # while meetings:
        # #     while meeting_rooms[0][0] >= 0 and meeting_rooms[0][0] <= curr_time:
        # #         curr_end, idx, num_meetings  = heapq.heappop(meeting_rooms)
        # #         heapq.heappush(meeting_rooms, (-1, idx, num_meetings))

        # #     if meeting_rooms[0][0] < 0:
        # #         curr_time = max(curr_time, meetings[0][0])
        # #         start, end = heapq.heappop(meetings)
        # #         curr_end, idx, num_meetings = heapq.heappop(meeting_rooms)
        # #         heapq.heappush(meeting_rooms, (curr_time+end-start, idx, num_meetings+1))
        # #     else:
        # #         curr_end, idx, num_meetings  = heapq.heappop(meeting_rooms)
        # #         curr_time = max(curr_time, curr_end)
        # #         heapq.heappush(meeting_rooms, (-1, idx, num_meetings))

        
        # # for i, (curr_end, idx, num_meetings) in enumerate(meeting_rooms):
        # #     meeting_rooms[i] = (-1, -num_meetings, idx)

        # # heapq.heapify(meeting_rooms)
        
        # # return meeting_rooms[0][2]

        # # Improved approach - Use two separate heaps to hold ongoing meetings and available_rooms

        # # meetings.sort()
        
        # # available_rooms = list(range(n))  # room indices
        # # heapq.heapify(available_rooms)
        
        # # ongoing_meetings = []  # (end_time, room_idx)
        # # room_usage = [0] * n
        
        # # for start, end in meetings:
        # #     # Free up rooms
        # #     while ongoing_meetings and ongoing_meetings[0][0] <= start:
        # #         _, room = heapq.heappop(ongoing_meetings)
        # #         heapq.heappush(available_rooms, room)
            
        # #     if available_rooms:
        # #         room = heapq.heappop(available_rooms)
        # #         heapq.heappush(ongoing_meetings, (end, room))
        # #         room_usage[room] += 1
        # #     else:
        # #         # Wait until the next room is free
        # #         next_end, room = heapq.heappop(ongoing_meetings)
        # #         duration = end - start
        # #         new_end = next_end + duration
        # #         heapq.heappush(ongoing_meetings, (new_end, room))
        # #         room_usage[room] += 1
        
        # # # Return the room with max meetings, break ties by room number
        # # max_meetings = max(room_usage)
        # # for i in range(n):
        # #     if room_usage[i] == max_meetings:
        # #         return i




                

                

           