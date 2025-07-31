class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        if not special:
            return top-bottom+1
        res = 0
        special.sort()

        res = special[0] - bottom
        for i in range(1, len(special)):
            curr_bottom = special[i-1]+1
            curr_top = special[i]-1
            res = max(res, curr_top-curr_bottom+1)
        res = max(res, top - special[-1])
    
        return res