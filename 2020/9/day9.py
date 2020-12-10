"""
"""

import timeit

LOOKBACK = 25  # use 5 for input2.txt testing


def read():
    with open("input.txt") as f:
        return f.read().splitlines()


def validate(items, target):
    for x in items:
        for y in items:
            if x + y == target and x != y:
                return True
    return False


def part1():
    look_range = []
    for index, line in enumerate([int(x) for x in read()]):
        look_range = look_range[-(LOOKBACK):]
        # print(index, line, look_range)
        look_range.append(line)
        if index > LOOKBACK:
            if not validate(look_range, line):
                return line


def part2():
    look_range = []
    TARGET = part1()  # use 127 for input2.txt

    data = [int(x) for x in read()]
    for x in range(0, len(data)):
        for y in range(0, len(data)):
            val = sum(data[x:y])
            if val == TARGET:
                return min(data[x:y]) + max(data[x:y])


def main():
    part1_ans = part1()
    part2_ans = part2()

    print(f"Part 1: {part1_ans}\nPart 2: {part2_ans}")


if __name__ == "__main__":
    print(timeit.timeit(main, number=1), "seconds")
