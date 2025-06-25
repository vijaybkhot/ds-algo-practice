class MyCalendar:

    def __init__(self):
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.bookings:
            self.bookings.append([startTime, endTime])
            return True
        else:
            booking_heap =[]
            temp = self.bookings.copy()
            temp.append([startTime, endTime])
            temp.sort()
            booking_heap.append(temp[0][1])
            heapq.heapify(booking_heap)
            
            for start, end in temp[1:]:
                if start >= booking_heap[0]:
                    heapq.heappop(booking_heap)
                heapq.heappush(booking_heap, end)
                if len(booking_heap) > 1:
                    return False
                
            self.bookings = temp
            return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)