class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # # Brute force solution:
        # res = [0]
        # temp_stack = [temperatures[-1]]

        # for i in range(len(temperatures)-2, -1, -1):
        #     curr_temp = temperatures[i]
        #     day_counter = 0
        #     catch_stack = []
        #     while temp_stack:
        #         next_temp = temp_stack.pop()
        #         day_counter += 1
        #         catch_stack.append(next_temp)
        #         if next_temp > curr_temp:
        #             res.append(day_counter)
        #             temp_stack.extend(catch_stack[::-1])
        #             catch_stack = []
        #             break
        #     # if No temp greater than curr temp found
        #     if len(catch_stack) != 0:
        #         res.append(0)
        #         temp_stack.extend(catch_stack[::-1])
        #     temp_stack.append(curr_temp)
        
        # return res[::-1]

        # Optimized solution using a monotonically decreasing stack
        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append([temp, index])
        
        return res


        