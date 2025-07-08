class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:

        # dp = {}
        
        # def dfs(x, y):
        #     if (x, y) in dp:
        #         return dp[(x, y)]
        #     if x == tx and y == ty:
        #         return 0
        #     if x > tx or y > ty:
        #         return float('inf')
            
        #     max_val = max(x, y)
        #     move_x = 1 + dfs(x+max_val, y)
        #     move_y = 1 + dfs(x, y+max_val)


        #     dp[(x, y)] = min(move_x, move_y)
        #     return dp[(x, y)]

        # res = dfs(sx, sy)
        # return res if res != float('inf') else -1

        # # Using BFS
        if sx == tx and sy == ty:
            return 0

        if sx == 0 and sy == 0:
            return -1

        # q = deque()
        # visited = set()
        # q.append((sx, sy, 0))

        # while q:
        #     x, y, steps = q.popleft()

        #     if (x, y) == (tx, ty):
        #         return steps

        #     if (x, y) in visited:
        #         continue
        #     visited.add((x, y))

        #     max_jump = max(x, y)
        #     if x + max_jump <= tx:
        #         q.append((x + max_jump, y, steps + 1))
        #     if y + max_jump <= ty:
        #         q.append((x, y + max_jump, steps + 1))

        # return -1

        if sx == 0 and sy == 0:
            return 0 if tx == ty == 0 else -1
        res = 0
        while (sx, sy) != (tx, ty):
            if sx > tx or sy > ty:
                return -1
            res += 1
            if tx > ty:
                if tx > ty * 2:
                    if tx % 2:
                        return -1
                    tx >>= 1
                else:
                    tx -= ty
            elif tx < ty:
                if ty > tx * 2:
                    if ty % 2:
                        return -1
                    ty >>= 1
                else:
                    ty -= tx
            else:
                if sx == 0:
                    tx = 0
                elif sy == 0:
                    ty = 0
                else:
                    return -1

        return res if (sx, sy) == (tx, ty) else -1