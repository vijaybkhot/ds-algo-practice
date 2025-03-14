class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        res = high

        def calcHours(piles, k):
            total_hours = 0
            for pile in piles:
                curr_hour = math.ceil(float(pile) / k)
                total_hours += curr_hour
            return total_hours

        while low <= high:
            mid = (low + high) // 2
            if calcHours(piles, mid) <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
    
        
        return res


            
            
        