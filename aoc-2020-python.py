import sys

import aoc2020_day1
import aoc2020_day2

if len(sys.argv) != 3:
    raise ValueError('Please specify the AOC day and part to be solved, e.g., to solve Day 1, Part 2: aoc-2020-python 1 2')
 
aoc_day = int(sys.argv[1])
aoc_part = int(sys.argv[2])

if aoc_day == 1:
    aoc2020_day1.solve(aoc_part)
elif aoc_day == 2:
    aoc2020_day2.solve(aoc_part)
else:
    print('No solution for Day ', aoc_day, ' Part ', aoc_part)
