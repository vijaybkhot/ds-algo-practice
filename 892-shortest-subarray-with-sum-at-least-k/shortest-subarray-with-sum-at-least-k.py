class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        mono_q = deque()
        prefix_sums = [0]
        res = len(nums) + 1

        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)


        for i, prefix in enumerate(prefix_sums):
            
            while mono_q and prefix - prefix_sums[mono_q[0]] >= k:
                res = min(res, i - mono_q.popleft())

            while mono_q and prefix_sums[mono_q[-1]] >= prefix:
                mono_q.pop()
            
            mono_q.append(i)

        return res if res <= len(nums) else -1

        # [-28, 81, -20,    28, -29]
        # -28,  53,   33,   61,   32
