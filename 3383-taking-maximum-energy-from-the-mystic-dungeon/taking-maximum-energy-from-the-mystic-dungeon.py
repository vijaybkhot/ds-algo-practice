class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        res = [0]*len(energy)

        for i in range(len(energy)-1, -1, -1):
            res[i] += energy[i]
            if i-k > -1:
                res[i-k] += res[i]

        return max(res)