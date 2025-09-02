class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                ax, ay = points[i]
                bx, by = points[j]

                # Condition: A is upper-left of B
                if ax <= bx and ay >= by:
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        cx, cy = points[k]

                        # Check if C lies inside/on the rectangle
                        if ax <= cx <= bx and by <= cy <= ay:
                            valid = False
                            break

                    if valid:
                        count += 1

        return count
