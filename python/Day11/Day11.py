# Day11.py
#
# First attempt at doing Day 11 of Advent of Code 2025

import time
import numpy as np
from collections import deque, defaultdict
from functools import cache


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    move_dict = defaultdict(list)
    for line in read_list:
        key, values = line.split(':')
        move_dict[key] = values.split()

    return move_dict


def run_dfs(graph, start):
    """
    @cache is equivalent to:
    ```
    def memoize(f):
        memo = {}
        def inner(n):
            if n not in memo:
                memo[n] = f(n)
            return memo[n]
        return inner
    ```
	"""

    @cache
    def dfs(node: str) -> int:
        if node == 'out':
            return 1
        return sum(dfs(neighbor) for neighbor in graph[node])

    return dfs(start)


def run_dfs2(graph: dict, start):
    @cache
    def dfs(node: str, fft: bool, dac: bool):
        if node == 'out':
            return 1 if (fft and dac) else 0
        return sum(dfs(neighbor, fft or neighbor  == 'fft', dac or neighbor == 'dac') for neighbor in graph[node])

    return dfs(start, False, False)


def dfs(graph, node):
    visited = []
    stack = deque()

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end = " ")

        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)


def bfs_optimize(adj_array, start, end):
    parent = {start: None}
    d = {start: 0}
    visited = []

    queue = deque()
    queue.append(start)
    #print(end)
    while queue:
        u = queue.popleft()
        if u not in visited:
            visited.append(u)
        for n in adj_array[u]:
            # print(n)
            # if u in end:
            #     print(f'Shortest path between {start} and {end} is {d[u]} steps.')
            #     return parent, d
            if n not in d:
                if n not in parent:
                    parent[n] = []
                parent[n].append(u)
                d[n] = d[u] + 1
                queue.append(n)
    return parent, d


def main():
    ## Part 1
    # a = read_input("Day11_test_input.txt")
    a = read_input("Day11_input.txt")
    answer = run_dfs(a, 'you')
    print(f'{answer} paths that go from you to out')


def main2():
    # Part 2
    # b = read_input("Day11_test_input2.txt")
    b = read_input("Day11_input.txt")
    answer2 = run_dfs2(b, 'svr')
    print(f'{answer2} paths that pass through fft and dac.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
