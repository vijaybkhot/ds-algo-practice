class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rad, dire = "Radiant", "Dire"
        n = len(senate)
        # # Solution I: Using a heap to get the player with current round
        # rad_heap = [idx for idx, char in enumerate(senate) if char == 'R']
        # dire_heap = [idx for idx, char in enumerate(senate) if char == 'D']

        # while rad_heap and dire_heap:
        #     if rad_heap[0] < dire_heap[0]:
        #         curr_player = heapq.heappop(rad_heap)
        #         # Eliminate upcoming dire senator
        #         heapq.heappop(dire_heap)
        #         if not dire_heap:
        #             return rad    
        #         # Add curr_player back to heap            
        #         heapq.heappush(rad_heap, curr_player+n)
        #     else:
        #         curr_player = heapq.heappop(dire_heap)
        #         # Eliminate upcoming dire senator
        #         heapq.heappop(rad_heap)
        #         if not rad_heap:
        #             return dire
        #         # Add curr_player back to heap
        #         heapq.heappush(dire_heap, curr_player+n)

        # return rad if rad_heap else dire

        # Solution II - Using two deques instead of heaps
        rad_q = deque([idx for idx, char in enumerate(senate) if char == 'R'])
        dire_q = deque([idx for idx, char in enumerate(senate) if char == 'D'])
        while rad_q and dire_q:
            if rad_q[0] < dire_q[0]:
                curr_player = rad_q.popleft()
                # Eliminate upcoming dire senator
                dire_q.popleft()
                if not dire_q:
                    return rad    
                # Add curr_player back to q            
                rad_q.append(curr_player+n)
            else:
                curr_player = dire_q.popleft()
                # Eliminate upcoming rad senator
                rad_q.popleft()
                if not rad_q:
                    return dire    
                # Add curr_player back to q            
                dire_q.append(curr_player+n)
                
        return rad if rad_q else dire

        

        
        

        