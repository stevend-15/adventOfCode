import numpy as np

class Node():

    def __init__(self, char, left, right, up, down, x, y):
        self.char = char
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.coords = (y,x)
        self.path_cost = 0
        self.parent = None

    def print_node(self):
        print(f"node of pos {self.coords}, char: {self.char},"
                f" path_cost: {self.path_cost}")

def reset_path_costs(ns):

    for key in ns.keys():
        ns[key].path_cost = 0

def trace_goal_path(goal_node, arr):

    arr.append(goal_node.coords)

    if (goal_node.coords == (0,0)):
        return arr

    goal_node = goal_node.parent

    return trace_goal_path(goal_node, arr)

def dijsktra(start, nodes):


    start_node = nodes[start]
    frontier=[start_node]
    reached={start_node.coords: start_node}        
    
    while (not len(frontier)==0):
        
        if len(frontier)>=1:
            frontier.sort(key = lambda x:  x.path_cost)
        
        current_node=frontier.pop(0)

        #goal condition
        if (current_node.char == '{'):
            #goal_path = trace_goal_path(current_node, [])
            #print(f"goal_path:\n{goal_path} ")
            return current_node.path_cost
            
        children = get_children(current_node, nodes)

        for child in children:

            #path pruning condition
            if (child.coords not in reached 
            or child.path_cost < reached[child.coords].path_cost):
                reached[child.coords]=child
                frontier.append(child)
                child.parent = current_node

    #fail rv
    return np.inf

def get_children(curr_node, nodes): 

    kids = []
    curr_cost = curr_node.path_cost + 1


    #if above pos and <= 1 distance
    if ( (curr_node.left != None) and 
            (ord(nodes[curr_node.left].char) <= ord(curr_node.char) + 1)):
        nodes[curr_node.left].path_cost = curr_cost
        kids.append(nodes[curr_node.left])

    #if below pos and <= 1 distance
    if (curr_node.right != None and 
            (ord(nodes[curr_node.right].char) <= ord(curr_node.char) + 1)):
        nodes[curr_node.right].path_cost = curr_cost
        kids.append(nodes[curr_node.right])

    #if right pos and <= 1 distance
    if (curr_node.up != None and 
            (ord(nodes[curr_node.up].char) <= ord(curr_node.char) + 1)):
        nodes[curr_node.up].path_cost = curr_cost
        kids.append(nodes[curr_node.up])

    #if left pos and <= 1 distance
    if (curr_node.down != None and 
            (ord(nodes[curr_node.down].char) <= ord(curr_node.char) + 1)):
        nodes[curr_node.down].path_cost = curr_cost
        kids.append(nodes[curr_node.down])

    return kids

def parse_input():
    #read input
    mat = []

    with open("input.txt", "r") as f:
        for line in f: 
            mat.append(list(line.strip()))

    f.close()

    return mat

def instantiate_nodes(matrix):

    #create nodes
    nodes = {}
    start_coords = None
    pt2_starts = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            char = matrix[i][j]

            if (char == 'E'):
                matrix[i][j] = '{'
                char = matrix[i][j]

            if (char == 'S'):
                start_coords = (i,j)
                matrix[i][j] = 'a'
                char = matrix[i][j]

            if (char == 'a'):
                pt2_starts.append( (i,j))

            if (j >= 1):
                left = (i,j-1)
            else:
                left = None

            if (j < len(matrix[0])-1):
                right = (i,j+1)
            else:
                right = None

            if (i >=1):
                up = (i-1,j)
            else:
                up = None

            if (i < len(matrix)-1):
                down = (i+1,j)
            else:
                down = None

            node = Node(char, left, right, up, down, j, i)
            nodes[(i,j)] = node

    return nodes, start_coords, pt2_starts

if __name__== "__main__":
       
    matrix = parse_input()

    ns, pt1_start, starts = instantiate_nodes(matrix)

    rv = dijsktra(pt1_start, ns) 
    print(f"part 1 answer: {rv}\n")

    #PT2 
    best = np.inf

    for start in starts:

        reset_path_costs(ns)
        steps = dijsktra(start, ns)
        
        if (steps < best):
            best = steps

    print(f"part 2 answer: {best} ")
