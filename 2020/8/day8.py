"""
"""

import timeit


def read():
    with open("input.txt") as f:
        return f.read().splitlines()


def proc(prog):
    ip = 0  # instruction pointer
    acc = 0  # accumulator
    prev = 0  # previous accumulator state
    oplist = []

    while True:
        op, arg = prog[ip].split(" ")
        arg = int(arg)

        print(f"{op} {arg}, ip:{ip}, acc:{acc}")
        if ip in oplist:
            print("infinite loop detected")
            break
        oplist.append(ip)

        if op == "nop":
            ip += 1
        if op == "acc":
            acc += arg
            ip += 1
        if op == "jmp":
            ip += arg


def main():
    proc(read())


if __name__ == "__main__":
    print(timeit.timeit(main, number=1), "seconds")
