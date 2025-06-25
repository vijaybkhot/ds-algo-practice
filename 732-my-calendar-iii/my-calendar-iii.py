class MyCalendarThree:

    def __init__(self):
        self.bookings = []
        self.max_overlap = 0

    def book(self, startTime: int, endTime: int) -> int:
        if not self.bookings:
            self.bookings.append([startTime, endTime])
            self.max_overlap = 1
        else:
            count = 1
            for start, end in self.bookings:
                if startTime < end and start < endTime:
                    count += 1
            self.bookings.append([startTime, endTime])
            self.bookings.sort(key= lambda x: x[0])
            booking_heap = [self.bookings[0][1]]
            heapq.heapify(booking_heap)
            for start, end in self.bookings[1:]:
                if start >= booking_heap[0]:
                    heapq.heappop(booking_heap)
                heapq.heappush(booking_heap, end)
            self.max_overlap = max(self.max_overlap, len(booking_heap))
                
        return self.max_overlap

        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)