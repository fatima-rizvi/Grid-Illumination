#!/bin/python3
import math
import os
import random
import re
import sys
# Create hash table with each lamp that stores every value that lamp lights. Then check each query and exlclude the lamps adjacent to the query
def checkLit(lamp, query):
    if query[0] == lamp[0] or query[1] == lamp[1]:
        return True
    row = lamp[0]
    col = lamp[1]
    col_dif = abs_val(query[0] - lamp[0])
    row_dif = abs_val(query[1] - lamp[1])
    if row_dif == col_dif:
        return True

    return False
# print(f"Short: {checkLit([4,3], [3,4])}")
# print(f"Short2: {checkLit([4,3], [7,5])}")
def abs_val(num):
    if num < 0:
        return num * -1
    return num
def on_lamps(lamps, query):
    good_lamps = []
    for lamp in lamps:
        if abs_val(lamp[0] - query[0]) >= 2 or abs_val(lamp[1] - query[1]) >= 2:
            good_lamps.append(lamp)
    # print(good_lamps)
    return good_lamps
def checkIllumination(N, lamps, queries):
    output = []
    for query in queries:
        lit_lamps = on_lamps(lamps, query) # For loop
        status = "DARK"
        for lamp in lit_lamps:
            if checkLit(lamp, query) == True:   #While
                status = "LIGHT"
        output.append(status)
    return output
# Complete the checkIllumination function below.
def checkIllumination2(N, lamps, queries):
    output = []
    grid = {}
    #Use tuples
    # print(f"N: {N}")
    for num in range(N): 
        grid[num + 1] = [tuple([(num + 1), (col + 1)]) for col in range(N)]
    # print(f"Grid: {grid}")
    for i in range(len(lamps)):
        lamps[i] = tuple(lamps[i])
    # print(lamps)
    lamp_light = {}
    for lamp in lamps:
        #Set up lamp_light lists
        lamp_light[lamp] = {}
        for square in grid[lamp[0]]:
            lamp_light[lamp][square] = True
        col_num = lamp[1] - 1
        for row, square in grid.items():
            # print(grid[row][col_num])
            lamp_light[lamp][grid[row][col_num]] = True
        #Diagonals in quadrant one (lamp as origin)
        row = lamp[0]
        col = lamp[1] - 1
        # print("Quadrant 1")
        while row < N and col < (N-1):
            row += 1
            col += 1
            # print(grid[row][col])
            lamp_light[lamp][grid[row][col]] = True 
        #Diagonals in quadrant four (lamp as origin)
        row = lamp[0]
        col = lamp[1] - 1
        while row > 1 and col < (N-1):
            row -= 1
            col += 1
            lamp_light[lamp][(grid[row][col])] = True
        # Diagonals in quadrant two (lamp as origin)
        row = lamp[0]
        col = lamp[1] - 1
        while row < N and col > 0:
            row += 1
            col -= 1
            lamp_light[lamp][grid[row][col]] = True
        # Diagonals in quadrant three (lamp as origin)
        row = lamp[0]
        col = lamp[1] - 1
        while row > 1 and col > 0:
            row -= 1
            col -= 1
            lamp_light[lamp][grid[row][col]] = True
        # print(f"Lamp light at lamp {lamp}: {lamp_light[lamp]}")
    # print(f"Lamp light: {lamp_light}")
    for query in queries:

        blackout = {}
        blackout[(tuple(query))] = 0 #query square
        blackout[(tuple([(query[0] + 1), (query[1] + 1)]))] = 0 # square to the upper right
        blackout[(tuple([(query[0] + 1), query[1]]))] = 0 # square above
        blackout[(tuple([(query[0] + 1), query[1] - 1]))] = 0 # square to the upper left
        blackout[(tuple([(query[0]), query[1] - 1]))] = 0 # square to the left
        blackout[(tuple([(query[0] - 1), query[1] - 1 ]))] = 0 # square to the lower left
        blackout[(tuple([(query[0] - 1), query[1]]))] = 0 # square below
        blackout[(tuple([(query[0] - 1), query[1] + 1]))] = 0 # square to the lower right
        blackout[(tuple([(query[0]), query[1] + 1]))] = 0 # square to the right
        #Do if blackout.get(lamp): Returns a value or None
        # print(f"blackout: {blackout}")
        check_lamps = []
        for lamp in lamps:
            if blackout.get(lamp) == 0:
                pass
            else:
                check_lamps.append(lamp)
        # print(f"Check lamps: {check_lamps}")
        check_lit = "DARK"
        for lamp in check_lamps:
            # print(f"Lamp: {lamp}")
            new_q = tuple(query)
            # if new_q in lamp_light[lamp]:
            if lamp_light[lamp].get(new_q):
                check_lit = "LIGHT"
        output.append(check_lit)
    # print(f"Output: {output}")
    return output
