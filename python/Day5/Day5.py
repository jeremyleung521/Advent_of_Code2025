# Day5.py
#
# First attempt at doing Day 5 of Advent of Code 2025

import time
import numpy as np
from tqdm.auto import tqdm

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    fresh_i = set()
    avail_i = set()
    swap = False
    for line in read_list:
        if line == '':
            swap = True
            continue

        if not swap:  # Fresh Ingredients
            [x, y] = line.split('-')
            fresh_i.add((int(x),int(y)))
            #fresh_i.update(set(range(int(x), int(y)+1)))
        else:  # Available Ingredients
            avail_i.add(int(line)) 

    return fresh_i, avail_i


def check_freshness(fresh_i, avail_i):
    count = 0
    for item in avail_i:
        for (x,y) in fresh_i:
            if x <= item <= y:
                count += 1
                break

    return count


def remove_dups(fresh_i):
    fresh_i = [[min(x,y), max(x,y)] for (x,y) in fresh_i]
    final = [[fresh_i[0][0], fresh_i[0][1]]]
    done = False
    for (x,y) in tqdm(fresh_i[1:]):
        for idx, (z, a) in enumerate(final):
            if x <= z and z <= y <= a:
                final[idx] = [x, a]
                done = True
                break
            elif x <= z and y >= a:
                final[idx] = [x, y]
                done = True
                break
            elif z <= x <= a and a <= y:
                final[idx] = [z, y]
                done = True
                break
            elif z <= x <= a and z <= y <= a:
                done = True
                break
        
        if not done:
            final.append([x,y])
        done = False

    return final

def return_max(input_list):
    max_cal = np.max(input_list)
    where = np.where(input_list == max_cal)[0][0]

    return [int(max_cal), where]


def return_top3(input_list):
    sorted_list = sorted(input_list, key=lambda x: -x)
    cal_sum = sum(sorted_list[0:3])
    where_three = np.where(input_list > sorted_list[3])[0]

    return [int(cal_sum), where_three]


def main():
    ## Part 1
    # fresh, avail = read_input("Day5_test_input.txt")
    fresh, avail = read_input("Day5_input.txt")
    answer = check_freshness(fresh, avail)
    print(f'{answer} fresh ingredients.')


def main2():
    # Part 2
    #fresh, _ = read_input("Day5_test_input.txt")
    #fresh, _ = read_input("Day5_test_input2.txt")
    fresh, _ = read_input("Day5_input.txt")
    prev = []
    while True:
        if prev != fresh:
            prev = fresh
            fresh = remove_dups(fresh)
        else:
            break
    answer2 = sum([y- x + 1 for (x,y) in fresh])
    print(f'{answer2} IDs are fresh.')


if __name__ == "__main__":
    ## Part 1
    # startTime = time.perf_counter()
    # main()
    # print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
