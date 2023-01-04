import time
import re

class Monkey():

    def __init__(self, idf, items, operation, dividend, 
            true_rec, false_rec):
        self.idf = idf
        self.items = items
        self.op = operation
        self.dividend = dividend
        self.true_rec = true_rec
        self.false_rec = false_rec
        self.num_inspections = 0

    def print_items(self): 
        print(f"Monkey {self.idf}: {self.items} ")

def print_round(monks):
    for m in monks:
        m.print_items()

def find_greatest_2(monks):

    first = monks[0].num_inspections
    sec = monks[1].num_inspections
    inspections = [x.num_inspections for x in monks]
    #print(f"\nmonkey inspections: {inspections}\n ")

    for i in range(2, len(monks), 1):

        smallest = min([first, sec])
        curr = monks[i].num_inspections  

        #print(f"is curr ({curr}) > smallest ({smallest})? : {curr > smallest} ")
        if (curr > smallest):
            
            if (smallest == first):
                first = curr
            else:
                sec = curr

    
        #print(f"first and second are now {first} and {sec} ")
    return first, sec


if __name__== "__main__":

    monkeys = [] #an array of monkey objs
       
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    f.close()

    lines = [x.strip() for x in lines]

    #iterate over lines and create monkey objs
                        #start, stop, step
    for i in range(0, len(lines), 7):


        idf = re.sub(r"[^0-9]", '', lines[i])
        items = re.sub(r"[^\w\s]", '', lines[i+1])
        items = list(map(int, items.split(' ')[2:]))
        op = lines[i+2].strip().split(' ')[3:]
        op = ' '.join(op)
        dividend = lines[i+3].split(' ')
        dividend = int(dividend[len(dividend)-1])
        true_rec = int(lines[i+4][len(lines[i+4])-1])
        false_rec = int(lines[i+5][len(lines[i+5])-1])
        monkey = Monkey(idf, items, op, dividend, true_rec, false_rec)
        monkeys.append(monkey)

    hashmap = dict()

    #for 20 rounds
    for i in range(1000):
         
        print(f"round {i}\n\n")
        #for each monkey 
        for monkey in monkeys: 

            #for each item of the monkey

            for item in monkey.items:
                #perform the operations
                old = item
                item = eval(monkey.op)

                #item = item // 3


                #pass the item
                if (item % monkey.dividend == 0): #true
                    monkeys[monkey.true_rec].items.append(item)
                else:
                    monkeys[monkey.false_rec].items.append(item)
                #record the inspection
                monkey.num_inspections+=1
            
            monkey.items.clear()

        print_round(monkeys)
        time.sleep(4)


    v1, v2 = find_greatest_2(monkeys)
    print(f"v1: {v1}, v2: {v2} ")

    print(f"monkey business: {v1 * v2} ")
