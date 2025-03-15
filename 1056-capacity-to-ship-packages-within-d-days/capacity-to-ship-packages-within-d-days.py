class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def calcDaysForCapacity(capacity, weights):
            curr_capacity = 0
            days = 1
            i = 0
            for index, weight in enumerate(weights):
                curr_capacity += weight
                if curr_capacity > capacity:
                    days += 1
                    curr_capacity = weight

            return days
        
        low, high = max(weights), sum(weights)
        res = high
        while low <= high:
            mid = (low + high) // 2
            if calcDaysForCapacity(mid, weights) <= days:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res
        
            

        