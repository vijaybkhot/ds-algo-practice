class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = [1<<i for i in range(n.bit_length()) if (n >> i) & 1]
        prefix = [0]*len(powers)
        prefix[0] = powers[0]
        for i in range(1, len(powers)):
            prefix[i] = powers[i]*prefix[i-1]

        res = []

        for start, end in queries:
            product = prefix[end] / prefix[start-1] if start > 0 else prefix[end]
            res.append(int(product)% (10**9 + 7))
        
        return res
