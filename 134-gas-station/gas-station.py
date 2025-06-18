class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        # # Brute force approach
        # isPossible = False
        # res = -1
        # if sum(cost) > sum(gas):
        #     return -1
        # for i in range(n):
        #     if gas[i] < cost[i] or gas[i]==0:
        #         continue

        #     if not isPossible:
        #         curr_gas = 0
        #         for j in range(i, i+n):
        #             idx = j % n
        #             curr_gas += gas[idx]
                    
        #             if curr_gas < cost[idx]:
        #                 break
        #             curr_gas = curr_gas - cost[idx]
        #             if idx == (i-1)%n and curr_gas >= 0:
        #                 isPossible = True
        #                 res = i
        #                 break
        #     else:
        #         break
        
        # return res if isPossible else -1
        if sum(gas) < sum(cost):
            return -1
        start = 0
        curr_surplus = 0

        for i in range(n):
            curr_surplus += gas[i] - cost[i]
            if curr_surplus < 0:
                # Can't reach station i+1 from current start
                # So reset start to i+1
                start = i + 1
                curr_surplus = 0

        return start