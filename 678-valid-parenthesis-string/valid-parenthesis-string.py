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
        
        # # Top-down DP solution
        # dp = {}
        # def dfs(i, left):
        #     if (i, left) in dp:
        #         return dp[(i, left)]
        #     if left < 0:
        #         return False
        #     if i >= len(s):
        #         return left == 0
            
        #     if self.isPossible:
        #         return.
        #     if s[i] == '(':
        #         dp[(i, left)] = dfs(i+1, left+1)
        #     elif s[i] == ")":
        #         dp[(i, left)] = dfs(i+1, left-1)
        #     else:
        #         dp[(i, left)] = (dfs(i+1, left) or
        #         dfs(i+1, left+1) or
        #         dfs(i+1, left-1))
        #     return dp[(i, left)]

        # return dfs(0, 0)

        # # Greedy solution - maintaining two left open values, minLeft and maxLeft
        # # The two values are the range of possible open left parens
        # # If the maximum range, i.e. maxLeft falls below 0, we return False
        # # If min Range falls below zero, we set it to 0 and continue. This keeps our total possible range Greater than zero
        # # In the end if 0 is part of the range, we return True, else False
        # minLeft, maxLeft = 0, 0
        # for char in s:
        #     if char == '(':
        #         minLeft, maxLeft = minLeft + 1, maxLeft + 1
        #     elif char == ')':
        #         minLeft, maxLeft = minLeft - 1, maxLeft - 1
        #     else:
        #         minLeft, maxLeft = minLeft - 1, maxLeft + 1
            
        #     if maxLeft < 0:
        #         return False
        #     if minLeft < 0:
        #         minLeft = 0
        
        # return minLeft == 0

        # Stack solution

        left, star = [], []
        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()
        
        while left and star:
            if left.pop() > star.pop():
                return False
        
        return not left

        