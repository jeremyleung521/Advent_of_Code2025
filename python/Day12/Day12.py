# Day12.py
#
# First attempt at doing Day 12 of Advent of Code 2025

import time
import numpy as np


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    numbers = [chr(c) for c in range(48,58)]

    all_shapes = {}
    conditions = []

    key = 0
    shape = []
    for iline, line in enumerate(read_list):
        match line:
            case "":
                all_shapes[key] = shape
                key = 0
                shape = []
            case _:
                final_chara = line[-1]
                match final_chara:
                    case '#' | '.':
                        shape.append([chara for chara in line])
                    case ':':
                        key = int(line[:-1])
                    case _ if final_chara in numbers:
                        grid, assignment = line.split(': ')
                        key = tuple(int(i) for i in grid.split('x'))
                        value = [int(i) for i in assignment.split(' ')]

                        conditions.append([key, value])


    properties = {}
    for key, shape in all_shapes.items():

        widths = [sum([1 if chara == '#' else 0 for chara in line])for line in all_shapes[key]]
        properties[key] = (min(widths), max(widths), sum(widths))

    # print(all_shapes, conditions, properties)

    return all_shapes, conditions, properties


def check_fit(all_shapes, conditions, properties):
    works = []
    for line in conditions:
        [(x,y), assignment] = line

        # Area check
        avail_area = x * y

        tot_area = 0
        minw_width, minw_height, minh_width, minh_height = 0, 0, 0, 0

        for co, (mins, maxs, area) in zip(assignment, properties.values()):
            tot_area += co * area
            minw_width += co * mins
            minw_height += co * maxs
            minh_width += co * maxs
            minh_height += co * mins

        # print(assignment, properties)
        # print(f'area {tot_area}, avail_area {avail_area}')
        # print(minw_width, minw_height, minh_width, minh_height)

        if tot_area > avail_area:
            works.append(False)
            continue

        # if not ((minw_width <= min(x,y) and minw_height <= max(x,y)
        #         or (minh_width <= max(x,y) and minh_height <= min(x,y)))):
        #     works.append(False)
        #     continue

        works.append(True)

    # print(works)

    # print(sum(works))

    return sum(works)

def main():
    ## Part 1
    # all_shapes, conditions, properties = read_input("Day12_test_input.txt")
    all_shapes, conditions, properties = read_input("Day12_input.txt")
    answer = check_fit(all_shapes, conditions, properties)
    print(f'{answer} number of shapes fit into the region under their respective tree.')
    # print(f'Elf {answer[1]+1} has {answer[0]} calories worth of food.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

