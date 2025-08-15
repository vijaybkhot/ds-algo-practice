class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

    # 1 -> 0 ->1
    # 1-> 0
    # 0, 1
    # indegree: [0: 1, 1: 1]

        indegree = defaultdict(int)
        graph = defaultdict(set)

        for u, v in prerequisites:
            graph[v].add(u)
            indegree[u] += 1
        
        q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            curr_node = q.popleft()
            for nei in graph[curr_node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        for i in range(numCourses):
            if indegree[i] > 0:
                return False
        
        return True


