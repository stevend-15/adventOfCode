import numpy as np
import pandas as pd 

if __name__== "__main__":

    matrix = []
    with open("input.txt", "r") as f:
        for line in f:
            matrix.append(np.array(list(line.strip()), dtype='int'))

    f.close()

    matrix = np.array(matrix)

    df = pd.DataFrame(matrix, 
            columns=["pos" + str(i) for i in range(len(matrix[0]))])

    gamma = '' #most common bit
    epsilon = '' #least common bit

    #oxygen rating = most common value or 1 if tied
    #co2 scrub rating = least common val or 0 if tied

    o2_df = df.copy()
    co2_df = df.copy()

    for col in df: 

        #get gamma and epsilon
        counts = df.value_counts(df[col].values)
        if (counts.loc[0] > counts.loc[1]):
            gamma+='0'
            epsilon+='1'
        else:
            gamma+='1'
            epsilon+='0'

        #get o2 rating
        if (len(o2_df) != 1):
            counts = o2_df.value_counts(o2_df[col].values)
            if (counts.loc[1] >= counts.loc[0]): 
                o2_df = o2_df[o2_df[col] == 1]
            else:
                o2_df = o2_df[o2_df[col] == 0]

        #get co2 rating
        if (len(co2_df) != 1):
            counts = co2_df.value_counts(co2_df[col].values)
            if (counts.loc[0] <= counts.loc[1]): 
                co2_df = co2_df[co2_df[col] == 0]
            else:
                co2_df = co2_df[co2_df[col] == 1]

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(f"part 1 answer: {gamma * epsilon} ")

    o2_rating = int(''.join(list(map(str, (o2_df.iloc[0].values)))), 2)
    co2_rating = int(''.join(list(map(str, co2_df.iloc[0].values))), 2)

    print(f"o2_rating:\n{o2_rating}\n co2_rating:\n{co2_rating} ")
    print(f"part 2 answer: {o2_rating * co2_rating} ")





       
    
