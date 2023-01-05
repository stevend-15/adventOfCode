import ast 

def read_input():

    arr = []
    with open("input.txt", "r") as f:
        for line in f:
            if (line.strip() == ''):
                continue
            arr.append(ast.literal_eval(line.strip()))
    f.close()

    return arr

def compare(elem1, elem2):

    if (type(elem1) is int and type(elem2) is int):
        return comp_ints(elem1, elem2)
    elif (type(elem1) is list and type(elem2) is list):
        return check_sublist(elem1, elem2)
    else: #mixed types

        rv = 0
        if (type(elem1) is int):
            rv = check_sublist([elem1], elem2)
        else:
            rv = check_sublist(elem1, [elem2])
        return rv

#returns 0 if left int gt right int aka not in order
#1 if equal
#2 if left lt right aka in order
def comp_ints(i1, i2):

    #out of order, stop
    if (i1 > i2):
        return 0

    if (i1 == i2): #need to continue
        return 1

    return 2 #in order, stop
    
#returns 0 if left side is bigger or elements not in order
#returns 1 if left side is smaller or elements in order
def check_sublist(l1, l2):

    max_len = max( len(l1), len(l2))
    for i in range(max_len):

        try:
            rv = compare(l1[i], l2[i])
        except IndexError:
            if (len(l1) < len(l2)):
                return 2
            else:
                return 0

        if (rv == 0 or rv == 2):
            return rv

    return 1

def bubbleSort(arr): 

    n = len(arr)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):

            rv = compare(arr[j], arr[j+1])
            if (rv == 0):
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if not swapped:
            return arr
    return arr

if __name__== "__main__":

    array = read_input()

    num_correct = 0
    pair_counter = 1
    #for each pair
    for i in range(0, len(array)-1, 2):
        a = array[i]
        b = array[i+1]

        rv = compare(a,b)

        if (rv == 2):
            num_correct+=pair_counter


        pair_counter+=1

    array.append( [[2]])
    array.append( [[6]])
    sorted_arr = bubbleSort(array)

    i1 = 0
    i2 = 0
    for i in range(len(sorted_arr)):
        if (sorted_arr[i] == [[2]]):
            i1 = i+1

        if (sorted_arr[i] == [[6]]):
            i2 = i+1

    print(f"part 1 answer:{num_correct} ")
    print(f"part 2 answer:{i1*i2} ")
