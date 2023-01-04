import numpy as np
import time
import math


def determine_winner(boards, nums):

    #for each number, mark each match in each matrix with a -1
    for n in nums:

        for b in boards:

            for i in range(b.shape[0]):

                row = b[i]

                for j in range(len(row)):
                    
                      
                    if (row[j]==int(n)):
#print(f"i=n: {i} = {int(n)}    ")

                        b[i][j]=-1

            bingo = check_bingo(b)
            if (bingo):
                winner = b
                print(f"winner:\n {winner}    ")
                return winner, n



def check_bingo(mat):

    #check rows
    for i in range(mat.shape[0]):

        row = mat[i]

        if (row[0]==-1 and row[1]==-1 and row[2]==-1 and row[3]==-1
                and row[4]==-1):
            return True

    #check transpose
    matT = mat.transpose()
    for i in range(matT.shape[0]):

        col = matT[i]
        if (col[0]==-1 and col[1]==-1 and col[2]==-1 and col[3]==-1
                and col[4]==-1):
            return True

    return False


if __name__=="__main__":
    
    boards = []

    with open("input.txt", 'r') as inFile:

        line = inFile.readline().strip()
        nums = line.split(",")

    
    counter = 2 
    while (counter!=602):
        
        board = np.loadtxt("input.txt", dtype='i', skiprows=counter, max_rows=5)
        boards.append(board)
        counter+=6
        
    #determine winning board    
    winning_board, winning_num = determine_winner(boards, nums)
    winning_num = int(winning_num)

    #find the answer
    sum_unmarked = 0

    for i in range(winning_board.shape[0]):

        row = winning_board[i]

        for j in range(len(row)):

            if (row[j]!=-1):
                sum_unmarked+=row[j]
    
    answer = int(sum_unmarked) + int(winning_num)
    print(f"sum * winning num: {sum_unmarked} * {winning_num} = {sum_unmarked * winning_num}")
    print(f"boards: \n{boards[len(boards)-1]}    ")
    



