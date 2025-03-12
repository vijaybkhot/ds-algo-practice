class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        # """
        # fleet_stack = []
        # for i in range(len(position)):
        #     curr_distance = target - position[i]
        #     curr_time = curr_distance/speed[i]
        #     backup_stack = []
        #     if not fleet_stack:
        #         fleet_stack.append([position[i], curr_time, 1])
        #         continue
        #     while fleet_stack and fleet_stack[-1][1] >= curr_time:
        #         curr_fleet = fleet_stack.pop()
        #         if position[i] < curr_fleet[0] and curr_time <= curr_fleet[1]:
        #             new_fleet = [position[i], curr_time, curr_fleet[2]+1]
        #             fleet_stack.append(new_fleet)
        #             fleet_stack.extend(backup_stack[::-1])
        #             break
        #         backup_stack.append(curr_fleet)
            
        # return len(fleet_stack)
        # Sorting the position and speed array based on the position in descending order
        combined_array = [[p,s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(combined_array)[::-1]:
            time = (target - p) / float(s) 
            if stack and time <= stack[-1]:  
                continue
            stack.append(time)
        
        return len(stack)
