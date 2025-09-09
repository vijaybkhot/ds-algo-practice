class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        # Count=0
        # Curr=4

        # [(5, 6)
        #
        MOD = 10**9 + 7            
        q = deque([(1+delay, 1+forget, 1)])

        for day in range(2, n+1): 
            while q and q[0][1] <= day:
                q.popleft()
            
            # left, right = 0, len(q)-1
            # num_people_share_secret_index = -1

            # while left <= right:
            #     mid = (left+right)//2
            #     if q[mid][0] <= curr_day:
            #         num_people_share_secret_index = mid
            #         left = mid + 1
            #     else:
            #         right = mid - 1
            sharers = sum(cnt for start, _, cnt in q if start <= day)



            if sharers > 0:
                q.append((day + delay, day + forget, sharers % MOD))

        
        return sum(cnt for _, _, cnt in q) % MOD