import re
TRAVEL_TIME = 1
OPEN_TIME = 1

class Valve():

    def __init__(self, name, flow, paths):
        self.name = name
        self.flow_rate = flow #pressure/min
        self.paths = paths
        self.open = 0
        

def report(time, table):
    print(f"\n===TIME: {time}===\n")

    for key, val in table.items():
        print(f"valve {key}: open: {val.open}; flow: {val.flow_rate} ")



if __name__== "__main__":

    name_to_obj = {}
    loc = None
       
    #read data
    with open("mini_input.txt", "r") as f:
        for line in f:
            line = re.sub(r"[^\w\s]", '', line) #remove punctuation
            split_line = line.strip().split(' ')
            name = split_line[1]
            flow = split_line[4]
            flow = re.sub(r"[^0-9]", '', flow) #remove 'rate' from flow rate
            paths = split_line[9:]

            v = Valve(name, flow, paths) 
            name_to_obj[v.name] = v

            #starting node
            if (len(name_to_obj) == 1):
                loc = v

            #print(f"paths: {paths} ")
            #print(f"flow: {flow} ")
            #print(f"line.split(): {line}")

    f.close()


    report(30, name_to_obj)

