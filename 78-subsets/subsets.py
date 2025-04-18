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

        # Solution using a for loop in dfs function

        # res = []
        # def dfs(start, path):
        #     res.append(path[:])

        #     for i in range(start, len(nums)):
        #         path.append(nums[i])
        #         dfs(i+1, path)
        #         path.pop()
        # dfs(0, [])
        # return res

        # # Solution using BFS
        # q = deque([[]])
        # for num in nums:
        #     for _ in range(len(q)):
        #         curr_path = q.popleft()
        #         q.append(curr_path + [num])
        #         q.append(curr_path)
        
        # return list(q)

        res = []

        def dfs(index, path):
            res.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
        
        dfs(0, [])
        return res








            
            
        