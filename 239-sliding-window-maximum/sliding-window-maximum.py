class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr_max = float('-inf')
        q = deque()
        for right in range(k):
            num = nums[right]
            while q and q[-1][0] <= num:
                q.pop()
            q.append((num, right))
        output = [q[0][0]]
        
        left = 0
        for right in range(k, len(nums)):
            num = nums[right]
            while q and q[-1][0] <= num:
                q.pop() 
            while q and q[0][1] <= left:
                q.popleft()
            q.append((num, right))
            output.append(q[0][0])
            left += 1
        
        return output

