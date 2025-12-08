# Day8.py
#
# First attempt at doing Day 8 of Advent of Code 2025

import time
import numpy as np
from itertools import combinations

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    final_list = [tuple(map(int, line.split(','))) for line in read_list]

    return final_list


def multiply_list(input_list):
    number = input_list[0]
    for val in input_list[1:]:
        number *= val

    return number


def euclidean_distance(x, y):
    return float(np.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2))


def calc_distances(input_list):
    pairwise_distances = {}
    for x, y in combinations(range(len(input_list)), 2):
        coord1 = input_list[x]
        coord2 = input_list[y]
        pairwise_distances[(min(x,y), max(x,y))] = euclidean_distance(coord1, coord2)

    pairwise_distances = {k: v for k, v in sorted(pairwise_distances.items(), key=lambda item: item[1])}
    return pairwise_distances


def loop(input_list, pairwise_distances, n_iters):
    circuits = []
    used = set()
    counter = 0
    for idx, (key, value) in enumerate(pairwise_distances.items()):
        if counter < n_iters:
            if key[0] not in used and key[1] not in used:
                circuits.append({key[0], key[1]})
            elif key[0] in used and key[1] not in used:
                for circuit in circuits:
                    if key[0] in circuit:
                        circuit.add(key[1])
            elif key[0] not in used and key[1] in used:
                for circuit in circuits:
                    if key[1] in circuit:
                        circuit.add(key[0])
            elif key[0] in used and key[1] in used:
                keep = None
                for jdx, circuit in enumerate(circuits):
                    if keep is None:
                        if key[0] in circuit and key[1] in circuit:
                            break
                        elif key[0] in circuit and key[1] not in circuit:
                            keep = circuit
                            pair = key[1]
                        elif key[0] not in circuit and key[1] in circuit:
                            keep = circuit
                            pair = key[0]

                    else:
                        try:
                            if pair in circuit:
                                remove = circuits.pop(jdx)
                                keep.update(remove)
                        except NameError:
                            pass

            used.add(key[0])
            used.add(key[1])
            counter += 1
        else:
            break

    # Add in the other "single" clusters
    # for item in range(len(input_list)):
    #     if item not in used:
    #         circuits.append({item})

    circuits.sort(key=lambda x: len(x), reverse=True)

    return circuits


def loop2(input_list, pairwise_distances, n_iters):
    circuits = [[]]
    used = set()
    counter = 0
    for idx, (key, value) in enumerate(pairwise_distances.items()):
        if len(circuits[-1]) < len(input_list):
            if key[0] not in used and key[1] not in used:
                circuits.append({key[0], key[1]})
            elif key[0] in used and key[1] not in used:
                for circuit in circuits:
                    if key[0] in circuit:
                        circuit.add(key[1])
            elif key[0] not in used and key[1] in used:
                for circuit in circuits:
                    if key[1] in circuit:
                        circuit.add(key[0])
            elif key[0] in used and key[1] in used:
                keep = None
                for jdx, circuit in enumerate(circuits):
                    if keep is None:
                        if key[0] in circuit and key[1] in circuit:
                            break
                        elif key[0] in circuit and key[1] not in circuit:
                            keep = circuit
                            pair = key[1]
                        elif key[0] not in circuit and key[1] in circuit:
                            keep = circuit
                            pair = key[0]

                    else:
                        try:
                            if pair in circuit:
                                remove = circuits.pop(jdx)
                                keep.update(remove)

                        except NameError:
                            pass

            used.add(key[0])
            used.add(key[1])
            counter += 1

            # print(input_list[key[0]])
            # print(input_list[key[1]])

            answer = input_list[key[0]][0] * input_list[key[1]][0]

            # print(counter)
            # print(circuits)

        else:
            break

    return circuits, answer


def main():
    ## Part 1
    # a = read_input("Day8_test_input.txt")
    a = read_input("Day8_input.txt")
    distance_matrix = calc_distances(a)
    # print(distance_matrix)
    circuits = loop(a, distance_matrix, 1000)
    answer = multiply_list([len(x) for x in circuits[:3]])
    print(answer)
    #print(f'Elf {answer[1]+1} has {answer[0]} calories worth of food.')


def main2():
    # Part 2
    # b = read_input("Day8_test_input.txt")
    b = read_input("Day8_input.txt")
    distance_matrix2 = calc_distances(b)
    circuits, answer2 = loop2(b, distance_matrix2, None)

    print(f'{answer2} cycles.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
