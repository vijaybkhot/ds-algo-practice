class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)
        for emp, mgr in enumerate(manager):
            graph[mgr].append(emp)
        
        time = 0
        q = deque()
        q.append((headID, 0))

        while q:
            node, t = q.popleft()
            time = max(time, t)
            for nei in graph[node]:
                q.append((nei, t + informTime[node]))

        
        return time
            

