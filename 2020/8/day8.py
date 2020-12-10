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
    res = True  # execution result

    while True:
        try:
            op, arg = prog[ip].split(" ")
            arg = int(arg)
        except:
            return res, acc

        # print(f"{op} {arg}, ip:{ip}, acc:{acc}")
        if ip in oplist:
            # print("infinite loop detected")
            res = False
            break
        oplist.append(ip)

        if op == "nop":
            ip += 1
        if op == "acc":
            acc += arg
            ip += 1
        if op == "jmp":
            ip += arg

    return res, acc


def main():
    # Part 1
    _, part1_acc = proc(read())

    # Part 2
    input_str = read()
    for index, data in enumerate(read()):
        op, arg = data.split(" ")
        arg = int(arg)

        if op == "jmp":
            test_data = input_str.copy()
            test_data[index] = "nop " + str(arg)
        else:
            continue
        result, part2_acc = proc(test_data)
        if result:
            break

    print(f"Part 1 answer: {part1_acc}")
    print(f"Part 2 answer: {part2_acc}")


if __name__ == "__main__":
    print(timeit.timeit(main, number=1), "seconds")
