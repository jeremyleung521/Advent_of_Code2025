# Day6.py
#
# First attempt at doing Day 6 of Advent of Code 2025

import time
import numpy as np
from itertools import accumulate


def add_list(input_list):
    number = input_list[0]
    for val in input_list[1:]:
        number += val

    return number


def multiply_list(input_list):
    number = input_list[0]
    for val in input_list[1:]:
        number *= val

    return number


def combine_list_str(input_list):
    b = input_list[0]
    for val in input_list[1:]:
        b += val

    return b


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    final_list = [[i] for i in map(int, read_list[0].split())]
    for entry in read_list[1:-1]:
        if entry != "":
            for idx, val in enumerate(entry.split()):
                final_list[idx].append(int(val))

    operator_dict = {'*': multiply_list, '+': add_list}
    operator_list = [operator_dict[entry] for entry in read_list[-1].split()]

    return final_list, operator_list


def read_input2(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    operator_dict = {'*': multiply_list, '+': add_list}
    operator_list = [operator_dict[entry] for entry in read_list[-1].split()][::-1]

    read_list2 = (combine_list_str(line_list) for line_list in list(map(list, zip(*read_list[:-1])))[::-1])

    final_list = []
    this_list = []
    for entry in read_list2:
        try:
            this_list.append(int(entry))
        except ValueError:
            final_list.append(this_list)
            this_list = []

    final_list.append(this_list)

    return final_list, operator_list


def run_operator(input_list, operator_list):
    output_list = [int(0)] * len(operator_list)

    for idx, (vlist, operator) in enumerate(zip(input_list, operator_list)):
        output_list[idx] = operator(vlist)

    return sum(output_list)

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
    # input_list, operator_list = read_input("Day6_test_input.txt")
    input_list, operator_list = read_input("Day6_input.txt")
    answer = run_operator(input_list, operator_list)
    print(f'{answer} is the sum.')


def main2():
    # Part 2
    # input_list2, operator_list2 = read_input2("Day6_test_input.txt")
    input_list2, operator_list2 = read_input2("Day6_input.txt")
    answer2 = run_operator(input_list2, operator_list2)
    print(f'{answer2} is the sum.')


if __name__ == "__main__":
    ## Part 1
    # startTime = time.perf_counter()
    # main()
    # print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
