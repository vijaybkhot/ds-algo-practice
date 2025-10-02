class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        inorder = defaultdict(int)
        for u, v in prerequisites:
            graph[v].add(u)
            inorder[u] += 1
        
        q = deque([i for i in range(numCourses) if inorder[i] == 0])

        while q:
            node = q.popleft()
            for u in graph[node]:
                inorder[u] -= 1
                if inorder[u] == 0:
                    q.append(u)
        for i in range(numCourses):
            if inorder[i] > 0:
                return False
        
        return True