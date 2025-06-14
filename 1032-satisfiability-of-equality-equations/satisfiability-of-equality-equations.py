class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x,  y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True




class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        var_set = set()
        # First process all "=="
        for equation in equations:
            var_1, sign_1, sign_2, var_2 = equation
            if sign_1 == sign_2:
                uf.union(var_1, var_2)
            


        for equation in equations:
            var_1, sign_1, sign_2, var_2 = equation
            root_1, root_2 = uf.find(var_1), uf.find(var_2)
            if sign_1 == sign_2 and root_1 != root_2 or sign_1 != sign_2 and root_1 == root_2:
                return False
        
        return True
                