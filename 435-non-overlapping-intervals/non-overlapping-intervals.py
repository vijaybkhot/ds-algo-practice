class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 1:
            return 0

        intervals.sort(key=lambda x: (x[0], x[1]))

        # # Solution using a graph and connected edges and indegree - Not correct for all cases - Time - O(n^2)
        # graph = defaultdict(set)
        # indegree = [0]*len(intervals)
        
        # for i in range(len(intervals)):
        #     start, end = intervals[i]
        #     j = i+1
        #     while j < len(intervals) and intervals[j][0] < end:
        #         graph[i].add(j)
        #         graph[j].add(i)
        #         indegree[i] += 1
        #         indegree[j] += 1
        #         j += 1
        
        
        # count = 0
        # while any(deg > 0 for deg in indegree):
        #     max_indegree = max(indegree)
        #     max_degree_node = indegree.index(max_indegree)

        #     for nei in graph[max_degree_node]:
        #         indegree[nei] -= 1
            
        #     indegree[max_degree_node] = 0

        #     count += 1
        # return count

        count = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev_end:
                prev_end = intervals[i][1]
            else:
                count += 1
                prev_end = min(prev_end, intervals[i][1])
        
        return count

            

            