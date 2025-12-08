# Day7.py
#
# First attempt at doing Day 7 of Advent of Code 2025
import re
import time
import numpy as np


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    final_list = [list(line) for line in read_list]

    return final_list


def combine_list_str(input_list):
    b = input_list[0]
    for val in input_list[1:]:
        b += val

    return b


def run_tachyon(input_list):
     prev_check_list = {int(idx) for idx, val in enumerate(input_list[0]) if val == 'S'}
     counter = 0
     for idx, line in enumerate(input_list):
         current_check_list = set()
         for val in prev_check_list:
             match line[val]:
                 case 'S' | '|':
                     current_check_list.add(val)
                 case '^':
                     line[val-1] = '|'
                     line[val+1] = '|'
                     current_check_list.add(val-1)
                     current_check_list.add(val+1)
                     counter += 1
                 case '.':
                     if input_list[idx-1][val] == 'S' or input_list[idx-1][val] == '|':
                         line[val] = '|'
                         current_check_list.add(val)

         prev_check_list = current_check_list

     final_output = []
     for line in input_list:
         final_output.append(combine_list_str(line))
         print(final_output[-1])

     return final_output, counter


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
    #a = read_input("Day7_test_input.txt")
    a = read_input("Day7_input.txt")
    new_map, answer = run_tachyon(a)
    print(f'{answer} splits occurred.')


def main2():
    # Part 2
    b = read_input("Day7_test_input.txt")
    # b = read_input("Day7_input.txt")
    answer2 = return_top3(b)
    print(f'Elves {answer2[1] + 1} have {answer2[0]} calories worth of food.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    # startTime = time.perf_counter()
    # main2()
    # print(f'{time.perf_counter() - startTime} sec.')
