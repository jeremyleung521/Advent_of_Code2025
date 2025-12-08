#!/bin/bash
# new_day.sh
# Quick Function to create a new day.
#

cp -rf DayX Day"$@" &&
cd Day"$@" &&
sed -e "s/DayX/Day$@/g" -e "s/Day X/Day $@/g" DayX.py > Day"$@".py &&
mv DayX_test_input.txt Day"$@"_test_input.txt &&
rm DayX.py &&
curl https://adventofcode.com/2025/day/$@/input --cookie "session=$(cat ../../cookies.txt)" -o Day"$@"_input.txt
