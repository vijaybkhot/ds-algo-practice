class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counter = Counter(nums)

        res = 0
        for num in counter:
            if num+1 in counter:
                res = max(res, counter[num]+counter[num+1])
            
            if num-1 in counter:
                res = max(res, counter[num]+counter[num-1])
        
        return res

        