class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(ship_capacity):
            days_for_curr_speed = 1
            curr_load = 0
            for w in weights:
                if curr_load + w > ship_capacity:
                    days_for_curr_speed += 1
                    curr_load = 0
                curr_load += w
            return days_for_curr_speed <= days
        
        l, r = max(weights), sum(weights)
        while l <= r:
            mid = (l+r)//2
            if canShip(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l

            