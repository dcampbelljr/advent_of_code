"""
"""

import timeit


def read():
    with open("input.txt") as f:
        return f.read().splitlines()


def part1(nav):
    # N = 0, E = 90, S = 180, W = 270
    face = 90  # initially facing east
    x = y = 0

    # little magic to split the action and value
    for action, value in map(lambda x: (x[0], int(x[1:])), nav):
        

        if action == "L":
            face = (face - value) % 360
        if action == "R":
            face = (face + value) % 360

        if action == "N" or (action == "F" and face == 0):
            y += value
        if action == "S" or (action == "F" and face == 180):
            y -= value
        if action == "E" or (action == "F" and face == 90):
            x += value
        if action == "W" or (action == "F" and face == 270):
            x -= value

        print(f'{action} \t{value} \t{face} \t{x} \t{y}')

    print(f"Part 1 Answer: {abs(x) + abs(y)}")


def main():
    part1(read())


if __name__ == "__main__":
    print(timeit.timeit(main, number=1), "seconds")
