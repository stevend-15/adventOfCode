if __name__=="__main__":
    
    ''' PART 1 '''
    num_incs=0
    measurements = []
    with open("day1Input.txt", 'r') as inputFile:
        for line in inputFile:
            measurements.append(int(line))
    
#measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    for i in range(len(measurements)-1):
        prev= measurements[i]
        curr = measurements[i+1]
        
        if (curr > prev):
            num_incs+=1
    
    print(f"num incs for part 1: {num_incs}")

    '''PART 2'''
    num_incs=0
    for i in range(len(measurements)-3):
        window0 = [measurements[i], measurements[i+1], measurements[i+2]]
        window1 = [measurements[i+1], measurements[i+2], measurements[i+3]]
        
        if (sum(window1) > sum(window0)):
            num_incs+=1
    
    print(f"num incs for part 2: {num_incs}")

