#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the checkIllumination function below.
def checkIllumination(N, lamps, queries):
    output = []
    grid = {}
    # col = 1
    # print(f"N: {N}")
    for num in range(N):
        grid[num + 1] = [[(num + 1), (col + 1)] for col in range(N)]
    # print(f"Grid: {grid}")
    lit = []
    lamp_nums = {}
    lamp_num = 0
    for lamp in lamps:
        lamp_nums[lamp_num] = lamp
        lamp_num += 1
    # print(f"Lamp nums: {lamp_nums}")
    lamp_light = {}
    lamp_num = 0
    for lamp in lamps:
        #Set up lamp_light lists
        lamp_light[lamp_num] = []
        for square in grid[lamp[0]]:
            # if square not in lit:
                # lit.append(square)
            lamp_light[lamp_num].append(square)
        col_num = lamp[1] - 1
        for row, square in grid.items():
            # print(grid[row][col_num])
            # if grid[row][col_num] not in lit:
                # lit.append(grid[row][col_num])
            lamp_light[lamp_num].append(grid[row][col_num])
        # diag_hor_right = lamp[0]
        # diag_vert_right = lamp[1]
        # while diag_hor_right <= N:
        #Diagonals in quadrant one (lamp as origin)
        row = lamp[0]
        col = lamp[1] - 1
        # print("Quadrant 1")
        while row < N and col < (N-1):
            row += 1
            col += 1
            print(grid[row][col])
            lamp_light[lamp_num].append(grid[row][col])
        #Diagonals in quadrant four (lamp as origin)
        row = lamp[0]
        col = lamp[1] - 1
        while row > 1 and col < (N-1):
            row -= 1
            col += 1
            lamp_light[lamp_num].append(grid[row][col])
        # Diagonals in quadrant two (lamp as origin)
        row = lamp[0]
        col = lamp[1] - 1
        while row < N and col > 0:
            row += 1
            col -= 1
            lamp_light[lamp_num].append(grid[row][col])
        # Diagonals in quadrant three (lamp as origin)
        row = lamp[0]
        col = lamp[1] - 1
        while row > 1 and col > 0:
            row -= 1
            col -= 1
            lamp_light[lamp_num].append(grid[row][col])
        # print(f"Lamp light at lamp {lamp_num}: {lamp_light[lamp_num]}")
        #Move onto the next lamp_num
        lamp_num += 1
    # print(f"Lamp light: {lamp_light}")
    for query in queries:
        blackout = []
        #add spots for the lamp to be off
        blackout.append(query) #query square
        blackout.append([(query[0] + 1), (query[1] + 1)]) # square to the upper right
        blackout.append([(query[0] + 1), query[1]]) # square above
        blackout.append([(query[0] + 1), query[1] - 1]) # square to the upper left
        blackout.append([(query[0]), query[1] - 1]) # square to the left
        blackout.append([(query[0] - 1), query[1] - 1 ]) # square to the lower left
        blackout.append([(query[0] - 1), query[1]]) # square below
        blackout.append([(query[0] - 1), query[1] + 1]) # square to the lower right
        blackout.append([(query[0]), query[1] + 1]) # square to the right
        # print(f"blackout: {blackout}")
        check_lamps = []
        for num, lamp in lamp_nums.items():
            if lamp in blackout:
                pass
            else:
                check_lamps.append(num)
        check_lit = "DARK"
        for lamp in check_lamps:
            if query in lamp_light[lamp]:
                check_lit = "LIGHT"
        output.append(check_lit)
    # print(f"Output: {output}")
    return output
    
print(check_illumination(8, [[4, 3], [4, 4]], [[3, 4], [7, 6]]))
print(check_illumination(8, [[1, 6], [5, 6], [7, 3], [3, 2]], [[4, 4], [6, 6], [8, 1], [3, 1], [2, 3]))
