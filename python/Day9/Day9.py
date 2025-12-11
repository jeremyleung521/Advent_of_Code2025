# Day9.py
#
# First attempt at doing Day 9 of Advent of Code 2025

import time
import numpy as np
from itertools import combinations, pairwise, product
from tqdm.auto import tqdm, trange
from math import comb


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    return [(int(line.split(',')[0]), int(line.split(',')[1])) for line in read_list]


def calc_area(x, y):
    x_diff = abs(y[1] - x[1]) + 1
    y_diff = abs(y[0] - x[0]) + 1

    return x_diff * y_diff


def calc_all(input_list):
    max_area = 0
    for x, y in combinations(input_list, 2):
        temp_area = calc_area(x, y)
        # print(temp_area, x, y)
        if temp_area > max_area:
            max_area = temp_area
            # print(x,y, temp_area)

    return max_area


def is_positive(line_tuple, check_value):
    """
    Check to see if the value is "under" the line or not.

    Parameters
    ----------
    line_tuple : tuple of tuple
        the coordinates of the endpoints of the line
    check_value : tuple
        coordinate of the point

    Returns
    -------
    bool : bool
        True if the point is to the right/below the line. Else, False.
    """
    pos = 0 if line_tuple[0][0] == line_tuple[1][0] else 1
    other = 1 if pos == 0 else 0

    min_x = min(line_tuple[0][other], line_tuple[1][other])
    max_x = max(line_tuple[0][other], line_tuple[1][other])

    if min_x <= check_value[other] <= max_x:
        if line_tuple[0][pos] <= check_value[pos]:
            return 1
        else:
            return 0
    else:
        # Doesn't matter since we're diagonal from the line
        return 2


def is_negative(line_tuple, check_value):
    """
    Check to see if the value is "above" the line or not.

    Parameters
    ----------
    line_tuple : tuple of tuple
        the coordinates of the endpoints of the line
    check_value : tuple
        coordinate of the point

    Returns
    -------
    bool : bool
        True if the point is to the left/above the line. Else, False.
    """
    pos = 0 if line_tuple[0][0] == line_tuple[1][0] else 1
    other = 1 if pos == 0 else 0

    min_x = min(line_tuple[0][other], line_tuple[1][other])
    max_x = max(line_tuple[0][other], line_tuple[1][other])

    if min_x <= check_value[other] <= max_x:
        if line_tuple[0][pos] >= check_value[pos]:
            return 1
        else:
            return 0
    else:
        # Doesn't matter since we're diagonal from the line
        return 2



def hash_edges(input_list):
    edges = {}
    for x, y in pairwise(input_list + [input_list[0]]):
        # print(x,y)
        if x[0] == y[0]:
            if x[1] < y[1]:  # Going right
                edges[(x,y)] = is_negative
            elif x[1] > y[1]:  # Going left
                edges[(x,y)] = is_positive
        elif x[1] == y[1]:
            if x[0] < y[0]:  # Going down
                edges[(x,y)] = is_positive
            elif x[0] > y[0]:  # Going up
                edges[(x,y)] = is_negative

    # print(edges)
    return edges

def hash_edges_reverse(input_list):
    edges = {}
    for x, y in pairwise(input_list + [input_list[0]]):
        # print(x,y)
        if x[0] == y[0]:
            if x[1] < y[1]:  # Going right
                edges[(x,y)] = is_positive
            elif x[1] > y[1]:  # Going left
                edges[(x,y)] = is_negative
        elif x[1] == y[1]:
            if x[0] < y[0]:  # Going down
                edges[(x,y)] = is_negative
            elif x[0] > y[0]:  # Going up
                edges[(x,y)] = is_positive

    # print(edges)
    return edges

def draw_stuff(input_list, edges):
    """
    Can't be used on the full input list, takes too long
    """
    shape = (max([i[0] for i in input_list])+1, max([i[1] for i in input_list])+1)

    if shape[0] >= 10000 and shape[1] >= 10000:
        raise ValueError('Too big of an array draw.')

    final_list = [(['.'] * shape[1]) for _ in range(shape[0])]

    for x in tqdm(input_list):
        # print(x)
        final_list[x[0]][x[1]] = '#'

    # Draw Edges
    for (x, y) in tqdm(edges.keys()):
        if x[0] == y[0]:
            for i in range(min(x[1], y[1])+1, max(x[1], y[1])):
                final_list[x[0]][i] = 'X'
        elif x[1] == y[1]:
            for i in range(min(x[0], y[0])+1, max(x[0], y[0])):
                final_list[i][x[1]] = 'X'

    # print(edges)
    # Draw stuff inside edges
    for x in trange(shape[0]):
        for y in trange(shape[1], leave=False):
            test = []
            check = True
            for key, value in edges.items():
                test.append(value(key, (x,y)))
                print(key, value, (x,y), test[-1])
                if value(key, (x,y)) == 0:
                    check = False

            if check and (not (all(i == 2 for i in test))) and final_list[x][y] == '.':
                final_list[x][y] = 'X'

    with open('part2_output.txt', 'w') as file:
        for line in final_list:
            print(line, file=file)


def calc_all2(input_list, edges):
    max_area = 0

    for j, k in tqdm(combinations(input_list, 2), total=comb(len(input_list), 2)):
        temp_area = calc_area(j, k)
        # print(temp_area, x, y)
        if temp_area > max_area:
            test_overall = True
            for x in trange(min(j[0], k[0]), max(j[0], k[0])+1, leave=False):
                for y in trange(min(j[1], k[1]), max(j[1], k[1])+1, leave=False):
                    test = []
                    check = True
                    for key, value in edges.items():
                        test.append(value(key, (x, y)))
                        # print(key, value, (x,y), test[-1])
                        if value(key, (x, y)) == 0:
                            check = False
                            break

                    if not check:
                        break

                    if not (check and (not (all(i == 2 for i in test)))):
                        test_overall = False

                if not test_overall:
                    break

            if test_overall:
                max_area = temp_area
            # print(j, k, temp_area)

    return max_area


def calc_all3(input_list, edges):
    max_area = 0

    for j, k in tqdm(combinations(input_list, 2), total=comb(len(input_list), 2)):
        temp_area = calc_area(j, k)
        print(temp_area, j, k)
        if temp_area > max_area:
            for x in [j[0], k[0]]:
                for y in [j[1], k[1]]:
                    check = True
                    test = []
                    for key, value in edges.items():
                        test.append(value(key, (x, y)))
                        print(key, value, (x,y), test[-1])
                        if value(key, (x, y)) == 0:
                            check = False
                            break

                    if all(i == 2 for i in test):
                        check = False
                        break

                if not check:
                    break

            if check and all(i > 0 for i in test):
                max_area = temp_area
                print(j,k, max_area)

            # print(j, k, max_area)

    return max_area


def main():
    ## Part 1
    # a = read_input("Day9_test_input.txt")
    a = read_input("Day9_input.txt")
    answer = calc_all(a)
    print(f'{answer} is the max area.')


def main2():
    # Part 2
    #b = read_input("Day9_test_input.txt")
    b = read_input("Day9_test_input2.txt")
    # b = read_input("Day9_input.txt")
    edges = hash_edges(b)
    draw_stuff(b, edges)
    answer2 = calc_all3(b, edges)
    print(f'{answer2} is the max area.')
    # print(f'Elves {answer2[1] + 1} have {answer2[0]} calories worth of food.')


if __name__ == "__main__":
    ## Part 1
    # startTime = time.perf_counter()
    # main()
    # print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')

