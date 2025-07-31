class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        prev = set()
        res = set()

        for num in arr:
            curr = {num}
            for p in prev: 
                curr.add(num | p)
            res.update(curr)
            prev = curr
        
        return len(res)