class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        prereq = defaultdict(set)
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for a, b in prerequisites:
            graph[a].add(b)
            indegree[b] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                prereq[neighbor].update(prereq[node])
                prereq[neighbor].add(node)
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)


            
        res = []
        for u, v in queries:
            if u in prereq[v]:
                res.append(True)
            else:
                res.append(False)
        
        return res
