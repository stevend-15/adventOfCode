import numpy as np

if __name__== "__main__":


        with open("input.txt", "r") as in_file:

            data = np.array(list(map(int, in_file.read().strip().split(","))))

        #data = np.array([3,4,3,1,2])

        print(f"initial state: {(data)} ")

        for i in range(256):

#            if (np.all(data)): #there are no zeroes
#                data = data -1 
#                #print(f"after day {i+1} : {data} ")
#                continue
            
            num_zeroes = 0
            for j in range(len(data)):
                if (data[j] == 0):
                    data[j] = 6
                    num_zeroes+=1
                else:
                    data[j]-= 1


            new_arr = np.full(num_zeroes, fill_value=8)
            data = np.append(data, new_arr) 

            #print(f"after day {i+1}: {data} ")

            print(f"day {i} complete ")

        print(f"len data after sim: {len(data)} ")
            

