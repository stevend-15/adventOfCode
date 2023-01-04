if __name__=="__main__":

    x, y = 0, 0 
    
#l = [('forward',5), ('down',5), ('forward',8), ('up', 3), ('down',8), ('forward',2)]

    '''Part 1 '''

    l=[]
    with open ("input.txt", 'r') as inFile:
        for line in inFile:
            line = line.strip()
            splitLine = line.split(" ")
            l.append( ( splitLine[0], int(splitLine[1])))
    
    for i in l:
        
        if (i[0]=='up'):
           y-=i[1]
        elif (i[0]=='down'):
           y+=i[1]
        else:
           x+=i[1]

    print(f"\nPart 1 answer is x*y: {x} * {y} = {x*y}")    

    '''Part 2'''
    x, y, aim = 0,0,0

    for i in l: 

        if (i[0]=='down'):
            aim+=i[1]
        elif (i[0]=='up'):
            aim-=i[1]
        else:
            x+=i[1]
            y+= (aim*i[1])



    print(f"\nPart 2 answer is x*y: {x} * {y} = {x*y}")    


