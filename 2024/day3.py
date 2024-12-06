import re


def part1():
    with open('./input/day3.txt', 'r') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            total += findMu(line)
        print(total)


def findMu(line):
    total = 0
    match = re.findall(r'mul\(\d+,\d+\)+', line)
    for m in match:
        x, y = re.findall(r'\d+', m)
        total += int(x) * int(y)
    return total


def part2():
    with open('./input/day3.txt', 'r') as f:
        line = ''.join(f.readlines())
        total = 0
        enabled = True
        match = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line)
        for m in match:
            if m == 'do()':
                enabled = True
            elif m == 'don\'t()':
                enabled = False
            else:
                if enabled:
                    x, y = re.findall(r'\d+', m)
                    total += int(x) * int(y)

        print(total)


part2()
