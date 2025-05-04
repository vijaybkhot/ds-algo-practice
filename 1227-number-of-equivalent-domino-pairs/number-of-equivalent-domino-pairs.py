class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes_set = [(x, y) if x <= y else (y, x) for x, y in dominoes]
        count = 0
        freq_count = defaultdict(int)
        for idx, dom_set in enumerate(dominoes_set):
            freq_count[dom_set] += 1

        for key in freq_count:
            if freq_count[key] > 1:
                count += math.comb(freq_count[key], 2)
        
        return count