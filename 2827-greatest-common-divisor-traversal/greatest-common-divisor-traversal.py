class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        # # Brute force approach
        # def gcdGreaterThanOne(num1, num2):
        #     return gcd(num1, num2) > 1
        
        # # Form a graph for edges having gcd greater than 1

        # graph = defaultdict(set)
        # for idx, num in enumerate(nums):
        #     graph[(num, idx)]

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if gcdGreaterThanOne(nums[i], nums[j]):
        #             graph[i].add(j)
        #             graph[j].add(i)
        # # Calculate the number of connected components
        # # return graph
        # visited = set()
        # def dfs(node):
        #     if node in visited:
        #         return 
        #     visited.add(node)
        #     for nei in graph[node]:
        #         if nei not in visited:
        #             dfs(nei)
        
        # dfs(0)

        # return len(visited) == len(nums)

        # Using union-find
        if 1 in nums and len(nums) > 1:
            return False

        def findPrimeFactors(num):
            factors = set()
            
            # Check for factor 2
            while num % 2 == 0:
                factors.add(2)
                num //= 2

            # Check for odd factors from 3 to sqrt(num)
            i = 3
            while i * i <= num:
                while num % i == 0:
                    factors.add(i)
                    num //= i
                i += 2

            # If num > 1, it's a prime greater than sqrt(num)
            if num > 1:
                factors.add(num)

            return factors


        uf = UnionFind()
        for num in set(nums):
            factors = list(findPrimeFactors(num))
            if factors:
                uf.union(num, factors[0])
            for i in range(1, len(factors)):
                uf.union(factors[i-1], factors[i])
        
        first_root = uf.find(nums[0])
        for num in nums:
            if uf.find(num) != first_root:
                return False
        
        return True
            

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootY] < self.rank[rootX]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1
        return True


            
            
            

        