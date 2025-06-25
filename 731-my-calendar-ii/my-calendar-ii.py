class MyCalendarTwo:

    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.bookings or len(self.bookings) == 1:
            self.bookings.append([startTime, endTime])
            self.bookings.sort()
            return True
        else:
            temp = []
            temp.append([startTime, endTime])
            for start, end in self.bookings:
                if startTime < end and start < endTime:
                    temp.append([start, end])
            
            temp.sort()
            booking_heap = []
            heapq.heappush(booking_heap, temp[0][1])
            for start, end in temp[1:]:
                if booking_heap[0] <= start:
                    heapq.heappop(booking_heap)
                heapq.heappush(booking_heap, end)
                if len(booking_heap) > 2:
                    return False
                
            self.bookings.append([startTime, endTime])
            return True


            # count = 0
            # for start, end in self.bookings:
            #     if startTime < end and start < endTime:
            #         count += 1
            #         if count >= 2:
            #             return False
            
            # self.bookings.append([startTime, endTime])
            # self.bookings.sort()
            # return True


        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)