import numpy as np

if __name__== "__main__":

    #read file in as np matrix
    matrix = []

    with open("mini_input.txt", "r") as inFile:
        for line in inFile: 
            matrix.append(np.array(list(line.strip()), dtype='int'))

    inFile.close()

    matrix = np.array(matrix)

    lowPts = []
    lowPtCoords = []

    #loop through each element and check if it's lowest out of adj neighbs

    for i in range(matrix.shape[0]): 
        for j in range(matrix.shape[1]): 

            lowerLeft=0
            lowerRight=0
            lowerUp=0 
            lowerDown = 0
            
            try: 
                if (matrix[i][j] < matrix[i][j-1]): 
                    lowerLeft = 1
            except IndexError: 
                lowerLeft = 1

            try: 
                if (matrix[i][j] < matrix[i][j+1]):
                    lowerRight = 1
            except IndexError: 
                lowerRight = 1

            try: 
                if (matrix[i][j] < matrix[i-1][j]):
                    lowerUp = 1
            except IndexError: 
                lowerUp = 1

            try: 
                if (matrix[i][j] < matrix[i+1][j]):
                    lowerDown = 1
            except IndexError: 
                lowerDown = 1

            if (lowerLeft and lowerRight and lowerUp and lowerDown):
                lowPts.append(matrix[i][j])
                lowPtCoords.append( (i,j))
                #matrix[i][j] = -1

    #sum the lowest points
    print(f"pt1 final answer: {sum(lowPts) + len(lowPts)} ")
    print(f"lowPtCoords: {lowPtCoords} ")

    ###Part 2 ###


def getBasinCount(mat, coordTuple): 

    #get coord neighbs


    #base case
    #if there are no neighbors
    if (mat[coordTuple[0]][coordTuple[1]] == 9):
        return 0


def getCoordNeighbs(mat, coordTuple):

    neighbs = []

    #if the neighbor does not equal 9 and the neighbor is greater than the low pt

    #left neighb
    try: 
        if (not mat[coordTuple[0]][coordTuple[1]-1] == 9
                and mat[coordTuple[0]][coordTuple[1]-1] > mat[coordTuple[0]][coordTuple[1]]
            neighbs.append( (coordTuple[0], coordTuple[1]-1))
    except IndexError: 
        pass

    #right neighb
    try: 
        if (not mat[coordTuple[0]][coordTuple[1]+1] == 9
                and mat[coordTuple[0]][coordTuple[1]+1] > mat[coordTuple[0]][coordTuple[1]]
            neighbs.append( (coordTuple[0], coordTuple[1]+1))
    except IndexError: 
        pass

    #upper neighb
    try: 
        if (not mat[coordTuple[0]-1][coordTuple[1]] == 9
                and mat[coordTuple[0]-1][coordTuple[1]] > mat[coordTuple[0]][coordTuple[1]]
            neighbs.append( (coordTuple[0]-1, coordTuple[1]))
    except IndexError: 
        pass

    #lower neighb
    try: 
        if (not mat[coordTuple[0]+1][coordTuple[1]] == 9
                and mat[coordTuple[0]+1][coordTuple[1]] > mat[coordTuple[0]][coordTuple[1]]
            neighbs.append( (coordTuple[0]+1, coordTuple[1]))
    except IndexError: 
        pass


