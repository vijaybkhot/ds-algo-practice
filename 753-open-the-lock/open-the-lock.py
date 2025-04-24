class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_neighbors(pos):
            pos_arr = [num for num in pos]
            adjacent = []
            for i in range(len(pos)):
                curr_num = int(pos_arr[i])
                next_num = 0 if curr_num == 9 else curr_num+1
                prev_num = 9 if curr_num == 0 else curr_num - 1
                pos_arr[i] = str(next_num)
                adjacent.append(''.join(pos_arr))
                pos_arr[i] = str(prev_num)
                adjacent.append(''.join(pos_arr))
                pos_arr[i] = str(curr_num)
            return adjacent

        deadends_set = set(deadends)

        if "0000" in deadends_set:
            return -1

        q = deque()
        visited = set()
        q.append("0000")
        visited.add("0000")
        dist = 0
        while q:
            for _ in range(len(q)):
                curr_node = q.popleft()
                if curr_node == target:
                    return dist
                neighbors = get_neighbors(curr_node)
                for neighbor in neighbors:
                    if neighbor in deadends_set or neighbor in visited:
                        continue
                    visited.add(neighbor)
                    q.append(neighbor)
            dist += 1
        
        return -1