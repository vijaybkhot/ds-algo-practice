class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rad, dire = "Radiant", "Dire"
        n = len(senate)
        
        rad_heap = [idx for idx, char in enumerate(senate) if char == 'R']
        dire_heap = [idx for idx, char in enumerate(senate) if char == 'D']
        

        while rad_heap and dire_heap:
            if rad_heap[0] < dire_heap[0]:
                curr_player = heapq.heappop(rad_heap)
                # Eliminate upcoming dire senator
                heapq.heappop(dire_heap)
                if not dire_heap:
                    return rad    
                # Add curr_player back to heap            
                heapq.heappush(rad_heap, curr_player+n)
            else:
                curr_player = heapq.heappop(dire_heap)
                # Eliminate upcoming dire senator
                heapq.heappop(rad_heap)
                if not rad_heap:
                    return dire
                # Add curr_player back to heap
                heapq.heappush(dire_heap, curr_player+n)

        return rad if rad_heap else dire
        

        
        

        