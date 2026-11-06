import grid
import time
start_time = time.time()

easy = [
    [None, None, None, None,None,None, None, None, None],
    [None, 9, None, None, 1,None,None, 3, None],
    [None, None, 6,None, 2, None, 7, None, None],
    [None, None, None, 3, None,4,None, None,None],
    [2, 1, None, None, None, None, None, 9, 8],
    [None, None, None, None, None, None,None,None, None],
    [None, None, 2, 5,None, 6, 4,None, None],
    [None, 8, None, None, None, None, None, 1, None],
    [None, None, None, None, None,None, None,None, None],
]


grid_easy = grid.Grid(9, 9, grid.matrix2grid(easy))

grid_easy.solve2()

print(grid_easy.visualMatrix())
print()
print("--- %s seconds ---" % (time.time() - start_time))
