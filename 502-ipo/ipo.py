class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        i = 0
        max_heap = []
        projects = list(zip(capital, profits))
        n = len(projects)
        projects.sort()

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)

        return w
            
            

        # # # First attempt - O(NlogN + KlogN) - Inefficient
        # # max_profit = []
        # # for i in range(len(profits)):
        # #     profit = profits[i]
        # #     investment = capital[i]
        # #     heapq.heappush(max_profit, (-profit, investment))
        
        # # for i in range(k):
        # #     stack = []
        # #     while max_profit and max_profit[0][1] > w:
        # #         stack.append(heapq.heappop(max_profit))

        # #     if max_profit:
        # #         net_profit, investment = heapq.heappop(max_profit)
        # #         w += -net_profit
        # #     else:
        # #         break

        # #     while stack:
        # #         heapq.heappush(max_profit, stack.pop())
        # # return w

        # # # Using sorting 
        # # projects = list(zip(capital, profits))
        # # projects.sort()

        # # max_profit_heap = []
        # # i = 0
        # # n = len(projects)

        # # for _ in range(k):
        # #     while i < n and projects[i][0] <= w:
        # #         heapq.heappush(max_profit_heap, -projects[i][1])
        # #         i += 1
        # #     if not max_profit_heap:
        # #         break
        # #     w += -heapq.heappop(max_profit_heap)

        # # return w 

        # i = 0
        # max_heap = []
        # projects = list(zip(capital, profits))
        # n = len(projects)
        # projects.sort()

        # for _ in range(k):
        #     while i < n and projects[i][0] <= w:
        #         heapq.heappush(max_heap, -projects[i][1])
        #         i += 1
        #     if not max_heap:
        #         break
        #     w += -heapq.heappop(max_heap)
        
        # return w













        