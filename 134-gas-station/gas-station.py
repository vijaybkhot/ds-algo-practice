class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

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