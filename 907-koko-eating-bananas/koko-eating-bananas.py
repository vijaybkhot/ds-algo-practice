class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(bananas_per_hr):
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / bananas_per_hr)
            return hours <= h
        
        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r)//2
            if canFinish(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
