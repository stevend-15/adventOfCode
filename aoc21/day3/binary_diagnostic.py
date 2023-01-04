def filter_list(index, bit, arr):

    for a in arr:

        if (a[index]==bit):

            arr.remove(a)

    return arr

if __name__=="__main__":
    

    '''Part 1 correct answer: 2640986'''
    gamma = ""
    epsilon = ""
    
    report = []
    
    '''
    report = ['00100', '11110', '10110', '10111', '10101', 
    '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    '''

    with open('input.txt', 'r') as inFile:
        for line in inFile:
            report.append(line.strip())
        
    zeroCounter = {}
    oneCounter = {}

    for i in range(len(report)): #each element of the list
        
        bStr = report[i]
#print(bStr)

        for j in range(len(bStr)):

            b = bStr[j]

            if (b=='0'):
                
                try: 
                    zeroCounter[j]+=1
                except KeyError: 
                    zeroCounter[j]=1

            else: 
                try:
                    oneCounter[j]+=1
                except KeyError:
                    oneCounter[j]=1
    '''
    print(f"zeroCounter: {zeroCounter}    ")
    print(f"oneCounter: {oneCounter}    ")
    '''


    for i in range(len(report[0])):
        
        try:
            if (zeroCounter[i] > oneCounter[i]):
                gamma+='0'
                epsilon+='1'
            else:
                gamma+='1'
                epsilon+='0'

        except KeyError:
            continue

    
    print(f"gamma: {gamma}")
    print(f"epsilon: {epsilon}")

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(f"gamma * epsilon: {gamma} * {epsilon} = {gamma*epsilon}")

    '''Part 2'''

    #oxygen generator rating
    report2 = report[:]

    
    for i in range(len(oneCounter)): #for each index within the counter dicts

        if (zeroCounter[i] > oneCounter[i]):
           report2 = filter_list(i, '1', report2) 
        else:
           report2 = filter_list(i, '0', report2)
    
    print(f"report2: {report2}")
