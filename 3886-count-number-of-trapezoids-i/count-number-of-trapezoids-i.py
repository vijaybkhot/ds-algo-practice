class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        def comb(n, r):
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        
        y_map = defaultdict(int)
        for x, y in points:
            y_map[y] += 1
        
        y_count_list = [comb(count, 2) for _, count in y_map.items() if count > 1]
        res = 0
        # Brute force ineffieient approach
        # for i in range(len(y_count_list)):
        #     for j in range(i+1, len(y_count_list)):
        #         res += y_count_list[i]*y_count_list[j]
        
        # The double sum: sum_{i=0}^{n-1} sum_{j=i+1}^{n-1} (a[i] * a[j])
        # is equal to: (sum(a)^2 - sum(a^2)) // 2
        # i.e., total_pairs = (total_sum^2 - sum_of_squares) // 2
        total = sum(y_count_list)
        total_sq = sum(x * x for x in y_count_list)
        
        res = ((total * total - total_sq) // 2) % MOD
        return res