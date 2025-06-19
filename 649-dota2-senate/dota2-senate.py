class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r_count, d_count = 0, 0
        rad, dire = "Radiant", "Dire"
        n = len(senate)
        for char in senate:
            if char == 'R':
                r_count += 1
            else:
                d_count += 1
        
        if r_count == 0:
            return dire
        elif d_count == 0:
            return rad
        
        senate_arr = [char for char in senate]
        rad_heap = [idx for idx, char in enumerate(senate) if char == 'R']
        dire_heap = [idx for idx, char in enumerate(senate) if char == 'D']
        heapq.heapify(rad_heap)
        heapq.heapify(dire_heap)

        while rad_heap and dire_heap:
            if rad_heap[0] < dire_heap[0]:
                curr_player = heapq.heappop(rad_heap)
                # Eliminate upcoming dire senator
                heapq.heappop(dire_heap)
                if not dire_heap:
                    return rad
                # Add curr_player back to heap
                max_rad_idx = max(rad_heap) if rad_heap else curr_player
                max_dire_idx = max(dire_heap)
                new_idx = max(max_rad_idx, max_dire_idx) + 1
                heapq.heappush(rad_heap, new_idx)
            else:
                curr_player = heapq.heappop(dire_heap)
                # Eliminate upcoming dire senator
                heapq.heappop(rad_heap)
                if not rad_heap:
                    return dire
                # Add curr_player back to heap
                max_rad_idx = max(rad_heap) 
                max_dire_idx = max(dire_heap) if dire_heap else curr_player
                new_idx = max(max_rad_idx, max_dire_idx) + 1
                heapq.heappush(dire_heap, new_idx)

        return rad if rad_heap else dire
        

        
        

        