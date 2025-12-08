# Day7.py
#
# First attempt at doing Day 7 of Advent of Code 2025
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
     #with open('part1_output.txt', 'w') as file:
     #    for line in input_list:
     #        final_output.append(combine_list_str(line))
     #        print(final_output[-1], file=file)

     return counter


def run_tachyon2(input_list):
    prev_check_list = {int(idx) for idx, val in enumerate(input_list[0]) if val == 'S'}
    n_width = len(input_list[0])
    prev_path_list = [int(0)] * len(input_list[0])
    for idx, line in enumerate(input_list):
        current_check_list = set()
        current_path_list = [int(0)] * n_width
        for val in prev_check_list:
            match line[val]:
                case 'S':
                    current_check_list.add(val)
                    current_path_list[val] = 1
                case '|':
                    current_check_list.add(val)
                    if prev_line[val] == '|':
                        current_path_list[val] += prev_path_list[val]
                case '^':
                    line[val - 1] = '|'
                    line[val + 1] = '|'
                    current_check_list.add(val - 1)
                    current_check_list.add(val + 1)

                    current_path_list[val-1] += prev_path_list[val]
                    current_path_list[val+1] += prev_path_list[val]
                    current_path_list[val] = 0
                case '.':
                    if prev_line[val] == 'S' or prev_line[val] == '|':
                        line[val] = '|'
                        current_check_list.add(val)
                        current_path_list[val] += prev_path_list[val]

        #print(idx, current_path_list)
        prev_check_list = current_check_list
        prev_path_list = current_path_list
        prev_line = line

    return sum(current_path_list)


def main():
    ## Part 1
    #a = read_input("Day7_test_input.txt")
    a = read_input("Day7_input.txt")
    answer = run_tachyon(a)
    print(f'{answer} splits occurred.')


def main2():
    # Part 2
    # b = read_input("Day7_test_input.txt")
    b = read_input("Day7_input.txt")
    answer2 = run_tachyon2(b)
    print(f'{answer2} possible paths.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
