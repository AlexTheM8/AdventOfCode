from functools import cache


@cache
def transform(v):
    if v == 0:
        return 1, None
    strVal = str(v)
    strValLen = len(strVal)
    if strValLen % 2 == 0:
        midpoint = strValLen // 2
        return int(strVal[:midpoint]), int(strVal[midpoint:])
    return v * 2024, None


@cache
def countStones(stone, blinksRemaining):
    s1, s2 = transform(stone)
    if blinksRemaining == 1:
        return 1 if s2 is None else 2
    count = countStones(s1, blinksRemaining-1)
    if s2 is not None:
        count += countStones(s2, blinksRemaining-1)
    return count


def part1and2(part2=False):
    with open('./input/day11.txt') as f:
        line = list(map(int, f.read().split()))
    blinks = 75 if part2 else 25
    stoneCount = 0
    for stone in line:
        stoneCount += countStones(stone, blinks)
    print(stoneCount)


part1and2(part2=True)
