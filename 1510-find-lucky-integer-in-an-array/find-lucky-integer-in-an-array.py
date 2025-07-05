class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        res = -1

        for num, freq in counter.items():
            if num == freq:
                res = max(res, num)
        
        return res
        