import string

if __name__== "__main__":

    letter_indicies = set()
    stack = {}
    
    part = (input("to what part would you like the answer? (choose 1 or 2): "))
    with open("input.txt", "r") as f:
        for line in f: 
            #print(f"line: {line} ")

            for i, char in enumerate(line):
                #print(f"char at i: {char}: {i} ")

                #read in the stack data
                if ('[' in line and char in string.ascii_letters):
                    letter_indicies.add(i)

                    if (i in stack):
                        stack[i].append(char)
                    else:
                        stack[i] = [char]
                
            #if we reach the lines containing stack id numbers
            index_line = ''.join(line.strip().split(' '))
            zip_list = []
            if(index_line.isnumeric()):
                sorted_indices = sorted(list(letter_indicies)) 
                #print(f"index line: {index_line}")
                zip_list = list(zip(sorted_indices, range(1, len(index_line)+1)))
                #print(f"zip_list:\n{zip_list} ")
                #print(f"int index line: {list(map(int, index_line))} ")

                for elem in zip_list: 
                    stack[elem[1]] = stack.pop(elem[0])
                #print(f"original stack:\n{stack}\n")

            #stack operations                                
            #['move', '1', 'from', '1', 'to' '2']
            if ('move' in line):

                instrc = line.strip().split(' ')

                count = int(instrc[1])
                origin = int(instrc[3])
                dest = int(instrc[5])

                if (part == '1'):
                    ''' PART 1 Version Here '''
                    for i in range(count):
                        stack[dest].insert(0, stack[origin].pop(0))
                        #print(f"moved one box from {origin} to {dest} ")
                        #print(f"curr stack:\n{stack} ")
                elif (part == '2'):
                    '''Part 2 Version Here'''
                    sliced = stack[origin][:count]
                    #print(f"removing subarray: {sliced} from {stack[origin]} to {stack[dest]}")
                    stack[origin] = stack[origin][count:]
                    stack[dest] = sliced + stack[dest] 
                    #print(f"moved one box from {origin} to {dest} ")
                    #print(f"curr stack:\n{stack}\n")
                else:
                    print(f"Error! You must enter '1' or '2' for part number! ")



    #print(f"final stack: {stack} ")

    answer = ""

    for key, val in stack.items():
        answer+=val[0]

    print(f"answer: {answer} ")


