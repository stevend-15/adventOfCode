import numpy as np
import pandas as pd

if __name__== "__main__":
    
    part = input("enter the desired part num (1 or 2):") 

    #read file in as np matrix
    matrix = []

    with open("input.txt", "r") as f:
        for line in f: 
            matrix.append(np.array(list(line.strip()), dtype='int'))

    f.close()

    matrix = np.array(matrix)

    df = pd.DataFrame(matrix, 
            columns=['col_' + str(i) for i in range(len(matrix[0]))])

    counter = 0
    max_scenic_score = 0

    for i in range(len(df)):
        for j in range(len(df.columns)):

            #condition for edge trees
            if (i != j and i == 0 or i == len(df) - 1 
                    or j == 0 or j == len(df.columns) -1):
                counter+=1
                continue

            elem = df.iloc[i,j]

            elem_row = df.iloc[i].values
            elem_col = df.iloc[:,j].values

            left_row = elem_row[:j]
            right_row = elem_row[j+1:]
            up_col = elem_col[:i]
            down_col = elem_col[i+1:]

            if (part == '2'):
                s1 = 0
                                    #start, stop, step
                for k in range(len(left_row)-1,-1, -1 ):
                    if (left_row[k] >= elem):
                        s1+=1
                        break

                    s1+=1
                    
                s2 = 0

                for k in range(len(right_row)):
                    if (right_row[k] >= elem):
                        s2+=1
                        break
                    s2+=1

                s3 = 0
                                #start, stop, step
                for k in range(len(up_col)-1,-1, -1 ):
                    if (up_col[k] >= elem):
                        s3+=1
                        break
                    s3+=1

                s4 = 0

                for k in range(len(down_col)):
                    if (down_col[k] >= elem):
                        s4+=1
                        break
                    s4+=1

                ssum = s1 * s2 * s3 * s4
                if (ssum > max_scenic_score):
                    max_scenic_score = ssum

            #print(f"tree score for df.iloc[{i},{j}]:\n" 
            #        f"left:{s1} * right:{s2} * up:{s3} * down:{s4}: {ssum}\n")
            elif (part == '1'):
                bool1 = [x < df.iloc[i,j] for x in left_row]
                bool2 = [x < df.iloc[i,j] for x in right_row]
                bool3 = [x < df.iloc[i,j] for x in up_col]
                bool4 = [x < df.iloc[i,j] for x in down_col]

                if (all(bool1) or all(bool2) or all(bool3) or all(bool4)):
                    counter+=1
            else:
                print(f"you entered a bad part num ")

#            print(f"elem_row:\n{elem_row} ")
#            print(f"elem_col:\n{elem_col}")
#            print(f"left_row:\n{left_row} ")
#            print(f"right_row:\n{right_row} ")
#            print(f"up_col:\n{up_col} ")
#            print(f"down_col:\n{down_col}\n\n")


    print(f"counter: {counter} ")
    print(f"max_scenic_score: {max_scenic_score} ")

