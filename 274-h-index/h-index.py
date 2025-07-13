class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # # Using Binary Search
        # def citations_greater_than(num):
        #     return sum(1 for citation in citations if citation >= num)
        
        # low, high = 0, len(citations)
        # res = low
        # while low <= high:
        #     mid = (low+high)//2
        #     if mid <= citations_greater_than(mid):
        #         res = mid
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        
        # return res

        # Using count sort
        count = [0]*(max(citations)+1)

        for citation in citations:
            count[citation] += 1
        
        remaining = len(citations)
        res = 0
        for i in range(len(count)):
            if remaining < i:
                break
            res = i
            if count[i] > 0:
                remaining -= count[i]
            
        
        return res

            
