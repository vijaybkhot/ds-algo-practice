class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # # Brute Force
        # ways = 0
        # pen_cost = 0
        # while pen_cost <= total:
        #     remainder = total - pen_cost
        #     pencil_cost = 0
        #     while remainder >= pencil_cost:
        #         pencil_cost += cost2
        #         ways += 1
        #     pen_cost += cost1
        
        # return ways

        ways = 0
        max_pens = total // cost1

        for pens in range(max_pens + 1):
            remaining = total - pens * cost1
            pencils = remaining // cost2
            ways += pencils + 1  # +1 includes the case with 0 pencils

        return ways