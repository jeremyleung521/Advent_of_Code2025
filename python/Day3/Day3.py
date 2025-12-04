# Day3.py
#
# First attempt at doing Day 3 of Advent of Code 2025

import time
import numpy as np
from itertools import dropwhile

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()
    
    final_list = np.asarray([[int(i) for i in line] for line in read_list])
    return final_list


def read_input2(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()
    
    final_list = [[int(i) for i in line] for line in read_list]

    return final_list


def find_max(input_list):
    final_sum = np.zeros((len(input_list)), dtype=int)
    left = np.argmax(input_list[:,:-1], axis=1)

    for idx, (row, ileft) in enumerate(zip(input_list, left)):
        right = np.argmax(row[ileft+1:])+ileft+1
        final_sum[idx] = int(f'{row[ileft]}{row[right]}')

    return final_sum, final_sum.sum()


def find_max2(input_list, digits=2):
    final_solution = [0] * len(input_list)
    for idx, row in enumerate(input_list):
        number = ''
        pmax = 0
        search_list = row
        #print(row)
        for j in range(-(digits-1), 0, 1):
            pmax = max(search_list[:j])
            number += f'{pmax}'
            search_list = list(dropwhile(lambda x: x < pmax, search_list))[1:]
            #print(search_list)
            #print(number)
        number += f'{max(search_list)}'
        #print(number)
        final_solution[idx] = int(number)
         
    return final_solution, sum(final_solution)


def main():
    ## Part 1
    #a = read_input("Day3_test_input.txt")
    a = read_input("Day3_input.txt")
    joltage, answer = find_max2(a, digits=2)
    print(f'{joltage} has a sum of {answer}.')


def main2():
    # Part 2
    #b = read_input2("Day3_test_input.txt")
    b = read_input("Day3_input.txt")
    joltage2, answer2 = find_max2(b, digits=12)
    print(f'{joltage2} has a sum of {answer2}')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
