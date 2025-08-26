class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_dia_index = 0
        max_dia = 0
        max_area = 0

        for idx, row in enumerate(dimensions):
            l, w = row
            dia = (((l**2) + (w**2))**0.5)
            area = l * w
            if dia > max_dia or (dia == max_dia and area > max_area):
                max_dia = dia
                max_area = area
        return max_area
