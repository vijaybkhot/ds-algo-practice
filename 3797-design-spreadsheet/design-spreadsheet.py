class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0]*26 for _ in range(rows)]
        

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.getCell(cell)
        self.sheet[row][col] = value
        

    def resetCell(self, cell: str) -> None:
        row, col = self.getCell(cell)
        self.sheet[row][col] = 0
        

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        references = formula.split('+')
        X = self.getVal(references[0])
        Y = self.getVal(references[1])
        return X+Y
        
            
    
    def getCell(self, cell):
        col = ord(cell[0])-ord('A')
        row = int(cell[1:])-1
        return (row, col)
    
    def getVal(self, reference):
        val = 0
        if reference[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            row, col = self.getCell(reference)
            val = self.sheet[row][col]
        else:
            val = int(reference)
        
        return val

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)