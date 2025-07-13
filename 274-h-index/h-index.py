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
        n = len(citations)
        count = [0] * (n + 1)
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1

        total = 0
        for i in range(n, -1, -1): 
            total += count[i]
            if total >= i:
                return i
        return 0