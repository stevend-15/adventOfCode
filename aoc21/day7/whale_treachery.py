import numpy as np
import math


def f(steps):
    
    total_fuel = 0
    for i in range(steps+1):
        total_fuel+=i

    return total_fuel


if __name__=="__main__":
    
    '''
    test_pos = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    
    median = int(np.median(test_pos))

    print(f" median of test_pos: {np.median(test_pos)}")

    fuel = 0

    for p in test_pos:

        diff = abs(p-median)
        fuel+=diff

    print(f" fuel: {fuel}")
    '''

    #Part 1 correct answer: 344297
    with open("input.txt", 'r') as inFile:

        pos = list(map(int, inFile.read().strip().split(",")))


    big_median = int(np.median(pos))
    print(f" big_median: {big_median}")

    fuel = 0
    for p in pos: 

        diff = abs(p-big_median)
        fuel+=diff

    print(f" fuel: {fuel}")

    #Part 2 correct answer: 97164301
    best_fuel = math.inf
    best_i = 0
    for i in range(2001):

        fuel = 0
        for p in pos:
            fuel+= f( abs(i-p) )
            
        if (fuel < best_fuel):
            best_fuel = fuel
            best_i = i

    print(f" best_fuel: {best_fuel}\n best_i: {best_i}")
