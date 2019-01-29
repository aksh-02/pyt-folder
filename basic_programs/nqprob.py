'''
# this method has been written for n=4 only but it can be changed to accommodate different numbers

n=4
board=[[0]*n for i in range(n)]
print(board)

def noconflict(board,cur_row,cur_col,n):
    # to check that the current row has no ones
    for j in range(cur_col):
        if board[cur_row][j]==1:
            return False

    # to cheks for the diagonals
    # \ diagonal
    k=1
    while cur_row-k>=0 and cur_col-k>=0:
        if board[cur_row-k][cur_col-k]==1:
            return False
        k+=1
    # / diagonal
    k=1
    while cur_row+k<n and cur_col-k>=0:
        if board[cur_row+k][cur_col-k]==1:
            return False
        k+=1

    return True

for i in range(n):
    board[i][0]=1
    for j in range(n):
        board[j][1]=1
        if noconflict(board,j,1,n):
            for k in range(n):
                board[k][2]=1
                if noconflict(board,k,2,n):
                    for l in range(n):
                        board[l][3]=1
                        if noconflict(board,l,3,n):
                            print(board)
                        board[l][3]=0
                board[k][2]=0
        board[j][1]=0
    board[i][0]=0 

'''

'''

# second method

# here we are using a more compact data structure in which we will have a one dimension array instead of two and each index in the array will contain the row no. of the queen been placed

# this method has been written for n=4 only but it can be changed to accommodate different numbers
n=4
board=[-1]*n
print(board)


def noconflict(col_num):
    for i in range(col_num):
        # no previous column has queen in the same
        if board[i]==board[col_num]:
            return False
        # this checks the diagonals and abs() has been used to check both \ and / diagonals
        if col_num-i==abs(board[col_num]-board[i]):
            return False
    return True

for i in range(n):
    board[0]=i
    for j in range(n):
        board[1]=j
        if not noconflict(1):
            continue
        for k in range(n):
            board[2]=k
            if not noconflict(2):
                continue
            for l in range(n):
                board[3]=l
                if noconflict(3):
                    print(board)

'''

'''
# third method

# here we are using recursive method
# here also we are using the compact data structure of a one dimension array

def noconflict(board,col_num):
    for i in range(col_num):
        # no previous column has queen in the same
        if board[i]==board[col_num]:
            return False
        # this checks the diagonals and abs() has been used to check both \ and / diagonals
        if col_num-i==abs(board[col_num]-board[i]):
            return False
    return True

# the recursive method to put queens on the board      
def rqueens(board,col_num,n):
    if col_num==n:
        return True
    else:
        for i in range(n):
            board[col_num]=i
            if noconflict(board,col_num):
                done=rqueens(board,col_num+1,n)
                if done==True:
                    return True
        return False 


n=0
while n<1 or n>10:
    n=int(input('enter a number n less than 10 for the size of board : '))

board=[-1]*n
rqueens(board,0,n)
print(board)

'''

'''
#fourth method
# another method that uses permutations

from itertools import permutations

n=0
while n<1 or n>10:
    n=int(input('enter a number for the size of the board : '))

# by taking permutations we have made sure that no two queens are in the same row

# we have checked for two queens on the same diagonal by using the fact that sum of co-ordinates for queen on '/' diagonal will be same and difference of co-ordinates for queen on '\' diagonal will be same

# if two queens are found on the  same diagonal set() would reduce the number from n and thus the below condition would not satisfy

solutions=0

for sol in permutations(range(n)):
    if n==len(set(sol[i]+i for i in range(n)))==len(set(sol[i]-i for i in range(n))):
        solutions+=1
        print(sol)

print('number of solutions is equal to : ',solutions)
'''

# fifth method
# here the data structure will be a 2-dimensional array and the method will be recuursive

n=0
while n<1 or n>10:
    n=int(input('enter a number for the size of the board : '))
board=[[0]*n for i in range(n)]
for i in board:
    print(i)

print('result\n')

def noconflict(board,row_num,col_num,n):
    for i in range(col_num):
        if board[row_num][i]==1:
            return False
    k=1
    while row_num-k>=0 and col_num-k>=0:
        if board[row_num-k][col_num-k]==1:
            return False
        k+=1
    k=1
    while row_num+k<n and col_num-k>=0:
        if board[row_num+k][col_num-k]==1:
            return False
        k+=1
    
    return True

def rqueens(board,col_num,n):
     if col_num==n:
         return True
     else:
         for i in range(n):
             board[i][col_num]=1
             if noconflict(board,i,col_num,n):
                 done=rqueens(board,col_num+1,n)
                 if done==True:
                     return True
             board[i][col_num]=0
         return False

rqueens(board,0,n)
for i in board:
    print(i)

