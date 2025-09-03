class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        res = 0

        for i in range(1, len(points)):
            bob_x, bob_y = points[i]
            prev_points = points[:i]
            j = len(prev_points)-1
            highest_left = float('inf')
            while j > -1:
                alice_x, alice_y = points[j]
                if alice_y >= bob_y and alice_y < highest_left:
                    highest_left = alice_y
                    res += 1
                j -= 1
        return res

