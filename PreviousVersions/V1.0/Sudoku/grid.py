class Cell:
    def __init__(self,row,col,value):
        self.col = col
        self.row = row
        self.value = value


class Grid:
    def __init__(self,height,width,elements = []):
        self.height = height
        self.width = width

        if not elements:
            for i_row_item in range(height):
                row = []
                for j_col_item in range(width):
                    row.append(Cell(i_row_item, j_col_item, None))
                elements.append(row.copy())
                row.clear()

        self.elements = elements

    def validRow(self,number,row):
        for i in range(self.width):
            cell = self.elements[row][i]
            if cell.value == number:
                return False

        return True


    def validCol(self,number,col):
        for i in range(self.height):
            cell = self.elements[i][col]
            if cell.value == number:
                return False
        
        return True


    def which3by3(self,row,col):
        '''
        returns the upperleft cell (row,col) of the given element's 3x3 
        '''
        block_row = (row // 3) * 3
        block_col = (col // 3 ) * 3

        return block_row, block_col

    def validBox(self,number,row,col):
        row_start, col_start = self.which3by3(row,col)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                cell = self.elements[i][j]
                if cell.value == number:
                    return False
        return True

    def validCell(self,number,row,col):
        if self.validRow(number,row) and self.validCol(number,col) and self.validBox(number,row,col):
            return True
        else:
            return False


    def findEmptyCell(self):
        for row in range(self.height):
            for col in range(self.width):
                cell = self.elements[row][col]
                if cell.value == None:
                    return row,col
        return None,None

    def solve(self):
        row,col = self.findEmptyCell()
        if row == None and col == None:
            return True
        cell = self.elements[row][col]
        for number in range(1,10): # 1,2,...,9
            if self.validCell(number,row,col):
                cell.value = number
                if self.solve():
                    return True
                else:
                    cell.value = None

        return False

    def visualMatrix(self):
        visual_matrix = []
        for row in range(self.height):
            visual_row = []
            for col in range(self.width):
                cell = self.elements[row][col]
                visual_row.append(cell.value)

            visual_matrix.append(visual_row.copy())
            visual_row.clear()

        return visual_matrix



def matrix2grid(matrix):
    new_matrix = []
    for row in range(len(matrix)):
        new_row = []
        for col in range(len(matrix[row])):
            new_row.append(Cell(row,col,matrix[row][col]))

        new_matrix.append(new_row.copy())
        new_row.clear()
    return new_matrix


