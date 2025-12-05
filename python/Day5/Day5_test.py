# https://github.com/RadzPrower/AdventOfCode2025/blob/master/Day05.py

import time

def main(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    fresh_ranges, ingredient_list = parse_data(read_list)
    result = "There are " + str(check_freshness(fresh_ranges, ingredient_list)) + " fresh ingredient IDs.\n"
    result += "There are " + str(potentially_fresh(fresh_ranges)) + " potential ingredients that could be fresh.\n"
    return result

# Parse the incoming data into a set of possible fresh IDs and a separate list of ingredients
def parse_data(data):
    fresh_ranges = []
    ingredient_list = []
    for i, line in enumerate(data):
        if line == '':
            ingredient_list = data[i+1:]
            break
        start, end = line.split('-')
        fresh_ranges.append([int(start), int(end)])
    fresh_ranges.sort()
    combined_ranges = []
    range_index = 0
    for current_range in fresh_ranges:
        if not combined_ranges:
            combined_ranges.append(current_range)
            continue
        start, end = combined_ranges[range_index]
        if current_range[0] > end:
            combined_ranges.append(current_range)
            range_index += 1
        elif current_range[1] > end:
            combined_ranges[range_index][1] = current_range[1]
    return combined_ranges, ingredient_list

# Check each item on the list against a fresh ingredient
def check_freshness(fresh_set, ingredient_list):
    count = 0
    for ingredient_id in ingredient_list:
        for current_range in fresh_set:
            if current_range[0] <= int(ingredient_id) <= current_range[1]:
                count += 1
    return count

# Check only for a total number of potentially fresh ingredients with no regard to inventory on hand
def potentially_fresh(fresh_ranges):
    count = 0
    for current_range in fresh_ranges:
        count += current_range[1] - current_range[0] + 1
    return count

if __name__ == "__main__":
    startTime= time.perf_counter()
    answer = main('Day5_input.txt')
    print(answer)
    print(f'{time.perf_counter() - startTime} sec')
