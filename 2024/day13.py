import re

with open('./input/day13.txt') as f:
    lines = f.read().splitlines()
# Format: (aX, aY), (bX, bY), (prizeX, prizeY)
machines = set()
for i in range(3, len(lines)+1, 4):
    a = tuple(map(int, re.findall(r'\d+', lines[i-3])))
    b = tuple(map(int, re.findall(r'\d+', lines[i-2])))
    prize = tuple(map(int, re.findall(r'\d+', lines[i-1])))
    machines.add((a, b, prize))


def part1and2(part2=False):
    coins = 0
    for m in machines:
        (ax, ay), (bx, by), (px, py) = m
        if part2:
            px += 10000000000000
            py += 10000000000000
        denom = ((ax * by) - (ay * bx))
        aVal = ((bx * -py) - (by * -px)) / denom
        bVal = ((-px * ay) - (-py * ax)) / denom
        if aVal.is_integer() and bVal.is_integer() \
                and 0 <= aVal and 0 <= bVal:
            coins += (3 * aVal) + bVal
    print(coins)


part1and2(part2=True)
