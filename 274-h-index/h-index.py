class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def citations_greater_than(num):
            return sum(1 for citation in citations if citation >= num)
        
        low, high = 0, len(citations)
        res = low
        while low <= high:
            mid = (low+high)//2
            if mid <= citations_greater_than(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return res
