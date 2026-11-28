import random

class Cell:
    def __init__(self,row,col,value):
        self.col = col
        self.row = row
        self.value = value


class Grid:
    def __init__(self,height,width,elements = None):
        self.height = height
        self.width = width

        if elements is None:
            elements = []

        if not elements:
            for i_row_item in range(height):
                row = []
                for j_col_item in range(width):
                    row.append(Cell(i_row_item, j_col_item, None))
                elements.append(row.copy())
                row.clear()

        self.elements = elements
        self.initSets()

    def initSets(self):

        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

        for row in range(self.height):
            for col in range(self.width):
                
                num = self.elements[row][col].value

                if num is not None:
                    box = (row // 3) * 3 + (col // 3)

                    self.rows[row].add(num)
                    self.cols[col].add(num)
                    self.boxes[box].add(num)


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

    def validCell2(self,number,row,col):
        box = (row // 3) * 3 + (col // 3)
        if number not in self.rows[row] and number not in self.cols[col] and number not in self.boxes[box]:
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
    
    def bestCell(self):


        best_candidates = None

        position = (None,None)


        for row in range(self.height):
            for col in range(self.width):
                cell = self.elements[row][col]

                if cell.value == None:
                    candidates = []
                    for num in range(1,10):
                        if self.validCell2(num,row,col):
                            candidates.append(num)

                    if best_candidates == None or len(best_candidates) > len(candidates):

                        best_candidates = candidates
                        position = (row,col)
                    
                    if len(best_candidates) == 1:
                       return position, best_candidates


        return position, best_candidates

    
    def updateGrid(self,row,col,number, addition):
        box = (row // 3) * 3 + (col // 3)

        if addition:
            self.rows[row].add(number)
            self.cols[col].add(number)
            self.boxes[box].add(number)
        else:
            self.rows[row].remove(number)
            self.cols[col].remove(number)
            self.boxes[box].remove(number)
    

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
    
    def solve2(self,randomise = False):
        position, candidates = self.bestCell()
        row,col = position
        
        if row == None and col == None:
            return True
        
        cell = self.elements[row][col]

        if randomise:
            random.shuffle(candidates)

        for num in candidates:
            cell.value = num
            self.updateGrid(row,col,cell.value,True)

            if self.solve2(randomise):
                return True
            else:
                self.updateGrid(row,col,cell.value,False)
                cell.value = None

        return False

    def visualMatrix(self):
        visual_matrix = []
        for row in range(self.height):
            visual_row = []
            for col in range(self.width):
                cell = self.elements[row][col]
                if cell.value == None:
                    visual_row.append(0)
                else:
                    visual_row.append(cell.value)

            visual_matrix.append(visual_row.copy())
            visual_row.clear()

        return visual_matrix

    def generatePuzzle(self):
        self.elements[0][0].value = random.randint(1,9)
        self.updateGrid(0,0,self.elements[0][0].value,True)
        self.solve2(randomise = True)
        return self

    def uniqueSolution(self, limit=2):
        position, candidates = self.bestCell()
        row, col = position

        # solution found
        if row is None and col is None:
            return 1

        # no solution found
        if not candidates:
            return 0

        cell = self.elements[row][col]
        solutions = 0

        for num in candidates:
            cell.value = num
            self.updateGrid(row,col,cell.value,True)

            solutions += self.uniqueSolution(limit)

            self.updateGrid(row,col,cell.value,False)
            cell.value = None

            if solutions >= limit:
                return limit

        return solutions


    def difficultySetting(self,difficulty):

        cells_to_visit = [(row,col) for row in range(9) for col in range(9)]
        random.shuffle(cells_to_visit)

        plus_or_minus = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

        if difficulty == 'easy':
            removing_number = 44

        elif difficulty == 'medium':
            removing_number = 50

        elif difficulty == 'hard':
            removing_number = 56

        removing_number += random.choice(plus_or_minus)

        self.generatePuzzle()

        for current_row, current_col in cells_to_visit[:removing_number]:

            current_val = self.elements[current_row][current_col].value 

            self.elements[current_row][current_col].value = None
            self.updateGrid(current_row, current_col, current_val, False)

            if self.uniqueSolution() != 1:
                self.elements[current_row][current_col].value = current_val
                self.updateGrid(current_row, current_col, current_val, True)

        return self
        
        # randomise a cell and make it None
        # solve the puzzle with backtracking 
        # if it has 1 solutionn keep the newly acquired None cell
        # if it has >1 sols, restore the number and try a diff cell
        # continue until a certain (randomised) threshold of cells have
        # been removed
        
        
    

def matrix2grid(matrix):
    new_matrix = []
    for row in range(len(matrix)):
        new_row = []
        for col in range(len(matrix[row])):
            new_row.append(Cell(row,col,matrix[row][col]))

        new_matrix.append(new_row.copy())
        new_row.clear()
    return new_matrix


    
    