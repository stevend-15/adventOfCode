import queue

if __name__== "__main__":

    q = queue.SimpleQueue()
    with open("input.txt", "r") as f:

        for line in f: 
            split_line = line.strip().split(' ')

            if (split_line[0] == 'noop'):
                q.put(0)
            else:
                q.put(0)
                q.put(int(split_line[1]))

    f.close()
    
    cycle = 1
    X = 1
    sig_strength_sum = 0
    msg = ""
    pos = 1
    for i in range(q.qsize()):
        sprite = [X, X+1, X+2]

        if ( ((cycle + 20) % 40) == 0):
            sig_strength_sum+=(cycle * X)

        if (pos in sprite):
            msg+='#'
        else:
            msg+='.'

        X+=q.get()

        cycle+=1
        pos+=1

        #reset pos and create newline for msg
        if ( (cycle-1) % 40 == 0):
            msg+="\n"
            pos = 1


    print(f"sig_strength_sum: {sig_strength_sum}\n")
    print(f"msg:\n{msg} ")
