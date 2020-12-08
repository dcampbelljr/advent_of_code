"""
https://adventofcode.com/2020/day/7

"""

import timeit
import re
from collections import namedtuple


def read():
    # input2.txt can be used test for part2 answer will be 126
    with open("input.txt") as f:
        return f.read().splitlines()


def parse_line(line):
    res = {}
    contents = namedtuple("contents", ["name", "qty"])
    pattern = re.compile(r"""^\s(?P<qty>\d)\s(?P<name>.*)\sbag[s.]*$""")
    values = line.split(" bags contain", 1)
    res["name"] = values[0]
    res["contents"] = {}
    # print(bag)
    for index, item in enumerate((values[1].split(","))):
        # print(item)
        if not item == " no other bags.":
            match = pattern.match(item)
            res["contents"][index] = {}
            res["contents"][index] = contents(match.group("name"), match.group("qty"))
        else:
            res["contents"][0] = {}
            res["contents"][0] = contents("end", 0)
    return res


def find_bag(name, data):
    ans = ""
    for line in data:
        for y in line["contents"].values():
            if y.name == name:
                # print(f'{line["name"]}:{y.name}')
                ans += line["name"] + ","
                res = find_bag(line["name"], data)
                if res != "":
                    ans += res
    return ans


def count_bags(name, data):
    ans = 1
    for line in data:
        if name == line["name"]:
            for y in line["contents"].values():
                ans += int(y.qty) * count_bags(y.name, data)
    return ans


def main():
    data = []

    for line in read():
        data.append(parse_line(line))

    result = find_bag("shiny gold", data).strip(",")
    # result is a string containings a comma separated 
    # list of values, lets eliminate duplicates
    part1 = []
    for item in result.split(","):
        part1.append(item)
    print(f"Part 1: {len(set(part1))}")

    result2 = count_bags("shiny gold", data)
    # I have an off by one error that I haven't figured out yet
    print(f"Part 2: {result2-1}")


if __name__ == "__main__":
    print(timeit.timeit(main, number=1), "seconds")
