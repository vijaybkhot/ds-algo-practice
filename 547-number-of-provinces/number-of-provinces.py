class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.parent = [-1] * len(isConnected)

        def find(x):
            if self.parent[x] < 0:
                return x
            self.parent[x] = find(self.parent[x])
            return self.parent[x]
        
        def union(x, y):
            if x == y:
                return
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            if self.parent[rootX] > self.parent[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootX] += self.parent[rootY]  
            self.parent[rootY] = rootX

            return True
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        provinces = 0
        for province in self.parent:
            if province < 0:
                provinces += 1
        return provinces


        