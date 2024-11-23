#board was copied from internet so a solution is guaranteed

sudoku = [[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]
#list of lists

def show(game):

    for i in range(len(game)):
        if i % 3 == 0 and i !=0:
            #every 3 lines, print a border
            print('- - - - - - - - -')
        for j in range(len(game[0])):
            #iterates over the current row
            # len(game[0]) is the width
            if j % 3 == 0 and j !=0: 
                print(" | ", end="") #doesn't print a new line
                #gives a border
            if j == 8:
                print(game[i][j])
            else:
                print(str(game[i][j]) + " ", end="") #gives spaces between mid values
#end = "" means to stay on same line
show(sudoku)
#works!!

def unfilled(sudoku): # find zeroes
    for y in range(len(sudoku)): #row
        for x in range(len(sudoku[0])): #column
            if sudoku[y][x] == 0:
                return (y , x)
#now we know positions of points we need to change
    return None #if no empty it returns none



def sol_check(game, num , pos): #game is the board
    #check row
    for i in range(len(game[0])):
        if game[pos[0]][i] == num and pos[1] != i: # pos[0] is the row
            #above line checks if there are duplicates in row
            return False
        
    #check col  
    for i in range(len(game)):
        if game[i][pos[1]] == num and pos[0] != i: # checks column
            return False
    
    #check square

    L_square = pos[1] //3 # left to right square position
    H_square = pos[0] //3 # height of square 
    #both of these combined tells us which square we are in

    #now loop in the box
    for i in range(H_square * 3, H_square*3 + 3): #for each y position in the current square
        for j in range(L_square * 3, L_square*3 + 3): #for each x position in current square
            if game[i][j] == num and (i,j) !=pos: #checking if duplicate
                return False
    
    return True # no duplicates in rows,column or box




def backtracker(grid):

    found = unfilled(grid)
    if not found:
        return True
    
    else: 
        row , col = found

    for i in range(1,10): 
        #try numbers 1,9 and if it is a solution, use that number
        if sol_check(grid, num = i, pos = (row,col)):
            grid[row][col] = i

            if backtracker(grid): # try backtracker on new board
                return True
            
            grid[row][col] = 0
    return False

print(show(sudoku))
backtracker(sudoku)
print(show(sudoku))

            



