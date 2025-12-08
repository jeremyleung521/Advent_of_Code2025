# Day4.py
#
# First attempt at doing Day 4 of Advent of Code 2025

import time
import numpy as np

check_nb = np.array([(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, +1), (1, -1), (1, 0), (1, 1) ])

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    final_list = np.asarray([[i for i in line] for line in read_list])

    return final_list


def check_neighbors(input_list, x, y):
    if input_list[x,y] != '@':
        return 0
    else:
        count = 0
        for coord in check_nb:
            try:
                check_coord = np.array([x,y]) + coord
                if np.all(check_coord >= 0) and input_list[*check_coord]== '@':

                    count += 1
                    
            except IndexError:
                continue

        if count >= 4:
            return 0
        else:
            return 1

def loop_all(input_list):
    count = 0
    remove_list = []
    for x in range(len(input_list)):
        for y in range(len(input_list[0])):
            remove = check_neighbors(input_list, x, y)
            if remove == 1:
                remove_list.append([x,y])
                count += 1

    for coord in remove_list:
        input_list[*coord] = '.'

    return count


def loop_multiple(input_list):
    pcount = -1
    count = 0
    while True:
        if pcount < count:
            diff = loop_all(input_list)
            pcount = count
            count += diff
        else:
            break

    return count


def main():
    ## Part 1
    #a = read_input("Day4_test_input.txt")
    a = read_input("Day4_input.txt")
    answer = loop_all(a)
    print(f'{answer} accessible rolls of paper.')


def main2():
    # Part 2
    # b = read_input("Day4_test_input.txt")
    b = read_input("Day4_input.txt")
    answer2 = loop_multiple(b)
    print(f'{answer2} accessible rolls of paper.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
