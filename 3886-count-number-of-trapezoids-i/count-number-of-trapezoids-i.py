class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        def comb(n, r):
            return math.comb(n, r) if n >= r else 0

        y_map = defaultdict(int)
        for x, y in points:
            y_map[y] += 1
        
        pair_counts = [comb(count, 2) for count in y_map.values() if count >= 2]
        
        total = sum(pair_counts)
        total_sq = sum(x * x for x in pair_counts)
        
        res = ((total * total - total_sq) // 2) % MOD
        return res