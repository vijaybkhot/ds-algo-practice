class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # def dfs(index, output):
        #     if index == len(nums):
        #         result.append(output)
        #         return
        #     include_subset = output + [nums[index]]
        #     exclude_subset = output
        #     dfs(index + 1, include_subset)
        #     dfs(index + 1, exclude_subset)

        # result = []
        # dfs(0, [])
        # return result

        # Solution using BFS
        q = deque([[nums[0]], []]) if nums else deque([])
        i = 1

        while i < (len(nums)):
            for _ in range(len(q)):
                curr_path = q.popleft()
                q.append(curr_path + [nums[i]])
                q.append(curr_path)
            i += 1
        
        return list(q)


            
            
        