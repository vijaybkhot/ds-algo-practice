class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        q = deque()
        left = 0
        max_len = 0 

        max_charge = 0
        curr_sum = 0

        for right in range(len(chargeTimes)):
            curr_charge = chargeTimes[right]
            curr_cost = runningCosts[right]

            while q and q[-1][0] <= curr_charge:
                q.pop()
            q.append((curr_charge, right))
            curr_sum += curr_cost
        
            while left <= right and ((q[0][0]) + ((right-left+1)*curr_sum)) > budget:
                curr_sum -= runningCosts[left]
                while q and q[0][1] <= left:
                    q.popleft()
                left += 1
            max_len = max(max_len, right-left+1)
        
        return max_len
            

                


        