"""
"""

import timeit

def read():
    with open('input.txt') as f:
        return f.read().splitlines()

def main():
    input_lst = sorted([int(x) for x in read()])
    joltage = 0
    one = 0
    three = 1 # builtin adapter is always three 

    for x in input_lst:
        if (x - joltage == 1):
            one += 1 
        if (x - joltage == 3):
            three += 1 
        joltage = x

    print(input_lst)
    print(f'Part 1: {one}, {three}, {one * three}')

if __name__ == '__main__':
    print(timeit.timeit(main, number=1), 'seconds')