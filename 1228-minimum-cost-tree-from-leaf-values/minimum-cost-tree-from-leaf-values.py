class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        # arr.sort()

        # q = deque([l_node for l_node in arr])
        # count = 0

        # while len(q) > 1:
        #     l1 = q.popleft()
        #     l2 = q.popleft()
        #     count += l1*l2
        #     q.append(max(l1, l2))
        
        # return count

        # heap = arr[::]
        # heapq.heapify(heap)

        # count = 0

        # while len(heap) > 1:
        #     l1 = heapq.heappop(heap)
        #     l2 = heapq.heappop(heap)
        #     count += (l1*l2)
        #     heapq.heappush(heap, max(l1, l2))
        # return count

        # stack = [float('inf')]
        # count = 0

        # for idx, num in enumerate(arr):
        #     while stack and stack[-1] <= num:
        #         mid = stack.pop()
        #         count += mid* min(num, stack[-1])
            
        #     stack.append(num)

        # while len(stack) > 2:  # keep sentinel and one element
        #     count += stack.pop() * stack[-1]

        # return count

        n = len(arr)

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == j:       # single leaf => no non-leaf cost
                return 0
            best = float('inf')
            for k in range(i, j):  # split into [i..k] and [k+1..j]
                cost = (dfs(i, k)
                        + dfs(k+1, j)
                        + max(arr[i:k+1]) * max(arr[k+1:j+1]))
                best = min(best, cost)
            return best

        return dfs(0, n - 1)