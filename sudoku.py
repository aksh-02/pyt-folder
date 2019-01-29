
sudoku=[[8,0,0,0,0,0,0,0,0],
[0,0,3,6,0,0,0,0,0],
[0,7,0,0,9,0,2,0,0],
[0,5,0,0,0,7,0,0,0],
[0,0,0,0,4,5,7,0,0],
[0,0,0,1,0,0,0,3,0],
[0,0,1,0,0,0,0,6,8],
[0,0,8,5,0,0,0,1,0],
[0,9,0,0,0,0,4,0,0]
]
print('initial board \n')
for i in sudoku:
    print(i)

def safe(digit,row_num,col_num):
     for i in range(9):
         if sudoku[row_num][i]==digit:
             return False

     for i in range(9):
         if sudoku[i][col_num]==digit:
             return False

     # checking the box
     for i in range((row_num//3)*3,(row_num//3)*3+3):
         for j in range((col_num//3)*3,(col_num//3)*3+3):
             if sudoku[i][j]==digit:
                 return False     
     return True
'''
def empty(row_num,col_num):
    return True if sudoku[row_num][col_num]==0 else False


# solving the sudoku
def recsud(row_num,col_num):
    if row_num==0:
        col_num+=1
    if col_num>=9:
        return True
    else:
        if not empty(row_num,col_num):
            row_num=(row_num+1)%9
            if row_num==0:
               col_num+=1               # this piece of code doesn't work fine
        for i in range(1,10):
            if safe(i,row_num,col_num):
                sudoku[row_num][col_num]=i
                done=recsud((row_num+1)%9,col_num)
                if done==True:
                    return True
                sudoku[row_num][col_num]=0
        return False

print('final result\n')
print(recsud(0,-1))
for i in sudoku:
    print(i)
'''

def nextempty(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[j][i]==0:
                return j,i
    return -1,-1

# solving sudoku
def sudfunc(sudoku):
    row_num,col_num=nextempty(sudoku)
    if row_num==-1:
        return True
    for d in range(1,10):
        if safe(d,row_num,col_num):
            sudoku[row_num][col_num]=d
            done=sudfunc(sudoku)
            if done==True:
                return True
            else:
                sudoku[row_num][col_num]=0
    return False

print('final result\n')
sudfunc(sudoku)
for i in sudoku:
    print(i)
