import math


def part1():
    distance = 0
    with open('2024/input/day1.txt', 'r') as f:
        lines = f.readlines()
        a, b = [], []
        for line in lines:
            x, y = line.split('   ')
            a.append(int(x))
            b.append(int(y))
        a.sort()
        b.sort()
        for i, _ in enumerate(a):
            distance += math.fabs(a[i] - b[i])
        print(distance)


def part2():
    similarity = 0
    with open('2024/input/day1.txt', 'r') as f:
        lines = f.readlines()
        a, b = [], []
        for line in lines:
            x, y = line.split('   ')
            a.append(int(x))
            b.append(int(y))
        for v in a:
            similarity += v * b.count(v)
        print(similarity)
