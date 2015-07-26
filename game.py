#!/usr/bin/python

'''
This is an implementation of the infamous game of throns/life.

Authors: Michael and Tyler
Date: July 25th, 2015
'''

import os
import time
import random

# Global constants
CYCLES = 250
SEED_CHANCE = 0.3
SLEEP_TIME = 0.25
MATRIX_SIZE = 20
DEAD = ' '
ALIVE = 'X'
TEMP_MATRIX = [[DEAD for i in xrange(MATRIX_SIZE)] 
        for i in xrange(MATRIX_SIZE)]


# Utility functions
def print_matrix(matrix):
    '''
    Prints a 2D list
    '''
    os.system('clear')
    for line in matrix:
        print line
    time.sleep(SLEEP_TIME)

def seed():
    '''
    Used to determine if a cell is alive or dead when seeding.
    '''
    if random.random() > SEED_CHANCE:
        return DEAD
    else:
        return ALIVE

# Global variable
life_matrix = [[seed() for i in xrange(MATRIX_SIZE)] 
        for i in xrange(MATRIX_SIZE)]

# Game rules
def is_alive(x, y):
    neighbors = 0
    # Tabulating number of neighbors
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            # Checking edge cases
            if i < 0 or i >= MATRIX_SIZE:
                continue
            if j < 0 or j >= MATRIX_SIZE:
                continue
            # Checking if at origin
            if i == x and j == y:
                continue
            # Tabulating neighbors
            if life_matrix[i][j] == ALIVE:
                neighbors += 1
    # Calculate if cell is alive or dead
    if neighbors < 2:
        return DEAD
    elif neighbors == 2:
        return life_matrix[x][y]
    elif neighbors == 3:
        return ALIVE
    else:
        return DEAD


if __name__ == '__main__':
    print_matrix(life_matrix)
    for generation in xrange(CYCLES):
        temp = TEMP_MATRIX
        for i in xrange(MATRIX_SIZE):
            for j in xrange(MATRIX_SIZE):
                temp[i][j] = is_alive(i, j)
        life_matrix = temp
        print_matrix(life_matrix)
    print_matrix(life_matrix)

