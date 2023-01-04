import time


if __name__=="__main__":

    with open("input.txt", 'r') as inFile:

        counter = 0
        for line in inFile:
            
            line = line.split(" | ")
            output = line[1].strip().split(" ")
            
            for o in output:
                if (len(o)==2 or len(o)==3 or len(o)==4 or len(o)==7):
                    counter+=1
            
            '''
            print(f" line: {line} \n")
            print(f" output: {output} \n")
            time.sleep(2)
            '''


        print(f" counter: {counter}")
