import time
import numpy as np






if __name__=="__main__":


    '''
    lines = [  ((0,9), (5,9)),  ((8,0), (0,8)), ((9,4), (3,4)), ((2,2), (2,1)), ((7,0), (7,4)), 
    ((6,4), (2,0)), ((0,9), (2,9)), ((3,4), (1,4)), ((0,0), (8,8)), ((5,5), (8,2))]
    
    '''
    lines = []
    with open("input.txt", 'r') as inFile:
        
        for line in inFile:
#print(line)
#time.sleep(2)
            splitLine = line.split(" -> ")
            split1 = splitLine[0].split(",")
            split2 = splitLine[1].split(",")

            lines.append( ((int(split1[0]), int(split1[1])), 
                        (int(split2[0]), int(split2[1].strip()))))

#print(f"lines: {lines} ") 

    ocean = {}

    

    for line in lines:  #line = ((7,0), (7,4))
#        print(f"\n line: {line}")
        l1 = line[0] #(7,0) 
        l2 = line[1] #(7,4)
        
        if (l1[0]==l2[0]): #x1==x2
            #do stuff
            
            diff = abs(l1[1]-l2[1])+1
            if (l1[1] > l2[1]):
                
                for i in range(diff):
                    
                    temp = (l2[0], l2[1]+i)
#                    print(f" temp: {temp}")

                    try: 
                        ocean[temp]+=1
                    except KeyError:
                        ocean[temp]=1
            else:
                
                for i in range(diff):

                    temp = (l2[0], l2[1]-i)
#                    print(f" temp: {temp}")
                    try: 
                        ocean[temp]+=1
                    except KeyError:
                        ocean[temp]=1
        elif (l1[1]==l2[1]): #y1==y2

            diff = abs(l1[0]-l2[0])+1
#            print(f" diff: {diff} ")

            
            if (l1[0] > l2[0]):
                
                for i in range(diff):
                    
                    temp = (l1[0]-i, l1[1])
#                    print(f" temp: {temp}")
                    try: 
                        ocean[temp]+=1
                    except KeyError:
                        ocean[temp]=1
            else:
 
                for i in range(diff):

                    temp = (l1[0]+i, l1[1])

#                    print(f" temp: {temp}")
                    try: 
                        ocean[temp]+=1
                    except KeyError:
                        ocean[temp]=1
        else: #x1!=x2 nor y1!=y2
#print(f" continued on {line}")
            continue

        
    #count the occurrences
    counter = 0

    for key, val in ocean.items():

        if (val >=2):
            counter+=1

#    print(f"\nocean: {ocean}")
    print(f" counter: {counter}")

