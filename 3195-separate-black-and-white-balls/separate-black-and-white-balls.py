class Solution:
    def minimumSteps(self, s: str) -> int:
        # count = 0
        # s_arr = [char for char in s]
        # first_right = len(s_arr)-1

        
        # first_left = 0
        # while first_left < len(s_arr) and s_arr[first_left] == '0':
        #     first_left += 1
        
        # right = len(s_arr) - 1
        # while right > first_left:
        #     while right > first_left and s_arr[right] == '1':
        #         right -= 1
        #     if right <= first_left:
        #         break
        #     space = right
        #     right -= 1
        #     while right > first_left and s_arr[right] == '1':
        #         right -= 1
        
        #     diff = space - right
        #     count += diff
        #     s_arr[right+1], s_arr[space] = s_arr[space], s_arr[right+1]

        # return count
                

        count = 0
        zeros = 0
        for i in reversed(s):
            if i == '0':
                zeros += 1
            else:
                count += zeros
        
        return count