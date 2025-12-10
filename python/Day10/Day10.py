# Day10.py
#
# First attempt at doing Day 10 of Advent of Code 2025
#
# Part 2 solution from https://www.reddit.com/r/adventofcode/comments/1pity70/comment/ntb5qjy/
# https://topaz.github.io/paste/#XQAAAQAkBwAAAAAAAAA0m0pnuFI8c/fBNAn6x25rtjDKyFC50Rb5gE6D5FZJsoHisykO81bArob78SRnh736cTJ41NLezS7kxle4Ro5fJ8qW54lMBKoXAc1Ijh8jxq203S7WoI6GYCI2lrfhyfTuc40mupGo+3MlcwUZySVU1PpfVInoyuM/oGOW/d5+wsQs/Lex+jV5u0KAvRWRgSfuYPUbUmKOSr42xmTAB754yn6qZG1QE1mwGG9VecuLaKuduf9uzyp81Vitvgnn2z+gxC8cTOze6YpTDVYBoUiOJwxk2F396Vd6Lhv1rwF9JDNHZ2PXTkXp68woakeiAB7Fb8Q2drtpl4FtovmuQg32gV6T5DANpcDsCAgdFmpdXAOC5lp67kIHnHsLs71YCO8WZyQj+Q9CfZOXT8w2bbvXt2huXTAQNdGMiKbZrcsn+B1fef5JkjRXPttAlKjHF/lLzf7lrkn9SwB4ywKstzezO6Rx4pRJ/u4KtHdwsQxuUM4cnToRq7R3Y57cgv8mDYk2RBT44eaT505+KhfbdH1K3LNBSLi7q0LqgVC1Mp//5z3BL0dLCbgc8xUhr8211WKIxX/oiNhAVpDkAbBMOnKgggUJ6fFipjRpMkX2fM6onNSU1LMcIoAqKGNpD2ee025gFAvoaHHDsR4r6S1fc4xbPK5o2yd59Xrh2apzwJIKPI7esLkWN6wEVpmlEHrvIb5gQwRoCSHLCiPDztUzniL6ad+NteJiDZacdW/47L2VEydMKwqZUwB69pVWOoQOYb91LCGI3hOAtzUge48CMB9dK+QCQU6ViD9GsNqI0LWsyR/Ik5qh/GoLbS/TlqL55hDztGQbNQu9pXfbGOdYRbtTQjONfJQbf47Kk4K8tFd4U9RlKI06ufo7VJUaFe/HqTh4RSxEpedaOEhqGEmbLyoxMlZ6nVzxofhzKEssaYu/QfS79hWUhsD+wCN5QfdvRQ8VrA00N8Wt28nGvgsdaSkMX661AzFURWSI+DT/zQdxaA==

import time
import numpy as np
from ast import literal_eval
from itertools import combinations

import scipy.optimize
from tqdm.auto import tqdm

from scipy.optimize import linprog


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    results = []
    options = []
    joltage = []

    for line in read_list:
        sline = line.split(' ')
        results.append([0 if i == '.' else 1 for i in sline[0][1:-1]])
        options.append([literal_eval(i) if len(i[1:-1]) > 1 else tuple([int(i[1:-1])]) for i in sline[1:-1]])
        joltage.append([int(i) for i in sline[-1][1:-1].split(',')])

    return results, options, joltage


def press_buttons(length, input_list):
    answer = [0] * length
    for option in input_list:
        for press in option:
            answer[press] += 1

    on_off = [i % 2 for i in answer]

    return on_off, answer


def check_combo(input_list, options):
    final_total = 0
    for line, option in tqdm(zip(input_list, options), total=len(input_list)):
        final_answer = 10
        length = len(line)
        for i in range(length):
            breaker = False
            for combo in tqdm(combinations(option, i), leave=False):
                answer, _ = press_buttons(length, combo)
                if answer == line:
                    if i < final_answer:
                        final_answer = i
                        breaker = True
                        break
                        # print(combo, final_answer)

            if breaker:
                break

        final_total += final_answer

    return final_total


def check_combo_jolt(input_list, options, joltage):
    final_total = 0
    for line, option, jolts in tqdm(zip(input_list, options, joltage), total=len(input_list)):
        # List of what changes for each button press does for each light
        A =  [[1 if n in buttons else 0 for buttons in option] for n in range(len(jolts))]

        opt = scipy.optimize.linprog([1]* len(option),
                                     A_eq=A,
                                     b_eq=jolts,
                                     bounds=(0, None),
                                     method='highs',
                                     integrality=1,
                                     )

        final_total += int(opt.fun)

    return final_total


def main():
    ## Part 1
    # results, options, _ = read_input("Day10_test_input.txt")
    results, options, _ = read_input("Day10_input.txt")
    # print(results, options)
    answer = check_combo(results, options)
    print(f'{answer} is the sum of minimal number of steps.')


def main2():
    # Part 2
    # results, options, joltage = read_input("Day10_test_input.txt")
    results, options, joltage = read_input("Day10_input.txt")
    answer2 = check_combo_jolt(results, options, joltage)
    print(f'{answer2} is the sum of minimal number of steps.')


if __name__ == "__main__":
    ## Part 1
    # startTime = time.perf_counter()
    # main()
    # print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
