class DetectSquares:

    def __init__(self):
        self.points_map = defaultdict(int)
        self.points_list = []

    def add(self, point: List[int]) -> None:
        self.points_map[tuple(point)] += 1
        self.points_list.append(tuple(point))

        

    def count(self, point: List[int]) -> int:
        count = 0
        px, py = point
        for x, y in self.points_list:
            if (abs(py - y) != abs(px-x)) or px == x or py == y:
                continue
            count += (self.points_map[(px, y)] *
                      self.points_map[(x, py)])
                      
        return count

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)