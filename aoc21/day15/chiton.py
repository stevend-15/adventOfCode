import numpy as np
import time
import heapq

class Node():

    def __init__(self, coord):
        self.coord=coord
        self.parent=None
        self.pathCost=0


    def __lt__(self, nxt):
        return self.pathCost < nxt.pathCost

if __name__=="__main__":
    
    matrix = []
    with open("test_input.txt", 'r') as inFile:

        for line in inFile:
            matrix.append(line.strip())



    print(f" matrix: {matrix}")

    print(f" last element: {matrix[9][9]}")
    #matrix[0][0]
    #      row col
    
    start = Node(matrix[0][0])

    frontier = [start]
    heapq.heapify(frontier)

    reached = {start.coords: start}

    while (not len(frontier)==0):

        frontier.sort(key=lambda x: x.pathCost)

        current = heapq.heappop(frontier)
        
        if (current.coords
