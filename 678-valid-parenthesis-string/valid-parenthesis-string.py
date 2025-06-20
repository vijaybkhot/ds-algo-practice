class Solution:
    def checkValidString(self, s: str) -> bool:
        # left_paren, right_paren, star_q = deque(), deque(), deque()
        # star_count = 0
        # for idx, char in enumerate(s):
        #     if char == '(':
        #         left_paren.append(idx)
        #     elif char == ')':
        #         right_paren.append(idx)
        #     elif char == '*':
        #         star_q.append(idx)
        
        # while left_paren and right_paren:
        #     if left_paren[0] < right_paren[-1]:
        #         left_paren.popleft()
        #         right_paren.pop()
        #         while star_q[0] < right_paren[0]:
        #             star_q.popleft()
        #         right_paren.popleft()
                

        #     elif right_paren[0] < left_paren[0]:
        #         if star_q:
        #             if start_[]
        #             start_[q].popleft()
        #             right_paren.popleft()
        #         else:
        #             return False
        
        # if left_paren:
        #     if len(left_paren) > star_count:
        #         return False
        # elif right_paren:
        #     if len(right_paren) > star_count:
        #         return False

        # return True
        self.isPossible = False
        target = len(s)//2

        @lru_cache(None)
        def dfs(i, left):
            if left < 0:
                return
            if i >= len(s):
                if not self.isPossible and left == 0:
                    self.isPossible = True
                return
            
            if self.isPossible:
                return

            if s[i] == '(':
                return dfs(i+1, left+1)
            elif s[i] == ")":
                return dfs(i+1, left-1)
            else:
                dfs(i+1, left)
                dfs(i+1, left+1)
                dfs(i+1, left-1)

        dfs(0, 0)
        return self.isPossible
        