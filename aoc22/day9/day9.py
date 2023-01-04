import math 

class Node():

    def __init__(self, name, x,y):
        self.name = name
        self.x = x
        self.y = y
        self.last_x = 0
        self.last_y = 0


def are_adj(n1, n2):

    ans = math.dist([n1.x, n1.y], [n2.x, n2.y]) 
    #print(f"adj: {ans} ")

    return ans <=1.5

def print_pos(n1, n2):
    print(f"{n1.name}:({n1.x},{n1.y})\n{n2.name}:({n2.x},{n2.y}) ")

def slope(n1,n2):
    return ((n2.y - n1.y) / (n2.x - n1.x))

if __name__== "__main__":

    visited = []

    H = Node('H', 0,0)
    T = Node('T', 0,0)

    visited.append( (0,0))

    with open("input.txt", "r") as f:

        for line in f:

            instr = line.strip().split(' ')
            d = instr[0]
            steps = int(instr[1])
            #print(f"\npos at start of instr:{instr}\n{print_pos(H,T)}")

            for i in range(steps):

                if (d=='R'):
                    H.last_x = H.x
                    H.last_y = H.y
                    H.x+=1
                elif (d=='L'):
                    H.last_x = H.x
                    H.last_y = H.y
                    H.x-=1
                elif (d=='U'):
                    H.last_x = H.x
                    H.last_y = H.y
                    H.y+=1
                else:
                    H.last_x = H.x
                    H.last_y = H.y
                    H.y-=1

                if (not are_adj(H, T)):

                    #print(f"not adj! ")
                    #diagonal
                    if (H.x != T.x and H.y != T.y):
                        #print(f"got here ")
                        T.x = H.last_x
                        T.y = H.last_y
                    else:
                        if (d=='R' or d=='L'):
                            T.x = H.last_x
                        else:
                            T.y = H.last_y

                if ( (T.x, T.y) not in visited):
                    visited.append( (T.x, T.y))

                #print(f"{print_pos(H,T)} ")
                #print(f"are H and T adj?: {are_adj(H,T)} ")
       
    f.close()

    print(f"len(visited): {len(visited)} ")
