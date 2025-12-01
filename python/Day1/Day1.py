# Day1.py
#
# First attempt at doing Day 1 of Advent of Code 2025

import time
import numpy as np


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    return read_list


def part1_protocol(read_list):
    dial = 50
    counter = 0
    for line in read_list:
        match line[0]:
            case 'L':
                dial -= int(line[1:])
            case 'R':
                dial += int(line[1:])
        dial = dial % 100
        if dial == 0:
            counter += 1
        
    return dial, counter


def part2_protocol(read_list):
    dial = 50
    counter = 0
    for line in read_list:
        extra = 0
        match line[0]:
            case 'L':
                # Double count when starting from 0
                if dial == 0:
                    extra -= 1

                dial -= int(line[1:])
                pass_zero = abs(int(dial//100))
                
                dial = dial % 100
                # Under count when landing at 0
                if dial == 0:
                    extra += 1
            case 'R':
                dial += int(line[1:])
                pass_zero = int(dial//100)                
                dial = dial % 100

        counter += pass_zero + extra
        
    return dial, counter


def main():
    ## Part 1
    #a = read_input("Day1_test_input.txt")
    a = read_input("Day1_input.txt")
    final_answer, counter = part1_protocol(a)
    print(f'Final number is {final_answer}, hitting 0 {counter} times.')


def main2():
    # Part 2
    #b = read_input("Day1_test_input.txt")
    b = read_input("Day1_input.txt")
    final_answer2, counter2 = part2_protocol(b)
    print(f'Final number is {final_answer2}, hitting 0 {counter2} times.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
