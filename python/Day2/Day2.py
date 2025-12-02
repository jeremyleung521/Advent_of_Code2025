# Day2.py
#
# First attempt at doing Day 2 of Advent of Code 2025

import time
import numpy as np
from tqdm.auto import tqdm, trange
from itertools import batched


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    return [tuple(sline.split('-')) for sline in read_list[0].split(',')]


def check_invalid(input_list):
    bad_list = [[] for _ in range(len(input_list))]
    for idx, (x, y) in enumerate(input_list):
        for val in range(int(x), int(y)+1):
            val = str(val)
            tot_length = int(len(val)/ 2)
            if val[:tot_length] == val[tot_length:]:
                bad_list[idx].append(int(val))

    n_total = sum([sum(i) for i in bad_list])
    return bad_list, n_total 


def check_invalid2(input_list):
    count = 0
    for idx, (x, y) in enumerate(tqdm(input_list, total=len(input_list))):
        for val in trange(int(x), int(y)+1, leave=False):
            val = str(val)
            full_length = len(val)
            for i in range(2, full_length+1):
                if full_length % i == 0:
                    tot_length = int(full_length/i)
                    ideal = val[:tot_length] * i
                    if ideal == val:
                        count += int(val)
                        break

    return count 


def main():
    ## Part 1
    #a = read_input("Day2_test_input.txt")
    a = read_input("Day2_input.txt")
    answer, total = check_invalid(a)
    print(total)
    #print(f'Elf {answer[1]+1} has {answer[0]} calories worth of food.')


def main2():
    # Part 2
    #b = read_input("Day2_test_input.txt")
    b = read_input("Day2_input.txt")
    total2 = check_invalid2(b)
    print(total2)
    #print(f'Elves {answer2[1] + 1} have {answer2[0]} calories worth of food.')


if __name__ == "__main__":
    ## Part 1
    #startTime = time.perf_counter()
    #main()
    #print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
