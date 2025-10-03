class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        inorder = defaultdict(int)

        for u, v in prerequisites:
            graph[v].add(u)
            inorder[u] += 1
        
        q = deque([i for i in range(numCourses) if inorder[i] == 0])
        res = []

        while q:
            node = q.popleft()
            res.append(node)
            for v in graph[node]:
                inorder[v] -= 1
                if inorder[v] == 0:
                    q.append(v)
        
        for i in range(numCourses):
            if inorder[i] > 0:
                return []
        
        return res