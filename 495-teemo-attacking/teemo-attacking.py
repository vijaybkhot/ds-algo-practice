class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        curr_end = -1

        for start in timeSeries:
            if start <= curr_end:
                overlap = curr_end - start + 1
                res -= overlap
            res += duration
            curr_end = start+duration-1
        return res
