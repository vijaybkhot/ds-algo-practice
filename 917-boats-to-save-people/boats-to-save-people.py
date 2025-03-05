class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        total_boats = 0
        people.sort()
        left, right = 0, len(people)-1

        while left <= right:
            if left < right:
                if people[left] + people[right] <= limit:
                    left += 1
                    right -= 1
                    total_boats += 1
                    continue
                elif people[right] <= limit:
                    right -= 1
                    total_boats += 1
                else:
                    left += 1
                    total_boats += 1
            elif left == right:
                if people[left] <= limit:
                    total_boats += 1
                    break

        
        return total_boats
                    
                
