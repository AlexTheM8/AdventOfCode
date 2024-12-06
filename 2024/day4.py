from itertools import product
from enum import Enum


class Direction(Enum):
    UP = 'u'
    RIGHT = 'r'
    DOWN = 'd'
    LEFT = 'l'


SEARCH_STRING = 'XMAS'


def localSearch(coord, searchSpace, searchIdx, directions):
    x, y = coord
    width, height = len(searchSpace), len(searchSpace[0])
    x1, y1 = x, y  # Next coords
    for d in directions:
        match d:
            case Direction.UP:
                if y == 0:
                    return 0
                y1 -= 1
            case Direction.RIGHT:
                if x == width - 1:
                    return 0
                x1 += 1
            case Direction.DOWN:
                if y == height - 1:
                    return 0
                y1 += 1
            case Direction.LEFT:
                if x == 0:
                    return 0
                x1 -= 1
    if searchSpace[x1][y1] == SEARCH_STRING[searchIdx]:
        if searchIdx == len(SEARCH_STRING) - 1:
            return 1
        return localSearch((x1, y1), searchSpace, searchIdx + 1, directions)
    return 0


def xSearch(coord, searchSpace):
    x, y = coord
    width, height = len(searchSpace), len(searchSpace[0])
    if x == 0 or y == 0 or x == width-1 or y == height-1:
        return 0

    bsNeighbors = (searchSpace[x-1][y-1], searchSpace[x+1][y+1])
    fsNeighbors = (searchSpace[x+1][y-1], searchSpace[x-1][y+1])
    cnt = 0
    if 'M' in bsNeighbors and 'S' in bsNeighbors and 'M' in fsNeighbors and 'S' in fsNeighbors:
        cnt += 1
    return cnt


def part1():
    # Find all instances of XMAS in word search
    with open('./input/day4.txt', 'r') as f:
        lines = f.read().splitlines()
        xmasCnt = 0
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == SEARCH_STRING[0]:
                    # Cardinal
                    for op in Direction:
                        xmasCnt += localSearch((i, j), lines, 1, [op])
                    # Diagonal
                    for dirs in product([Direction.UP, Direction.DOWN], [Direction.RIGHT, Direction.LEFT]):
                        xmasCnt += localSearch((i, j), lines, 1, dirs)

        print(xmasCnt)


def part2():
    with open('./input/day4.txt', 'r') as f:
        lines = f.read().splitlines()
        xmasCnt = 0
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                # Search for A and xSearch
                if c != 'A':
                    continue
                xmasCnt += xSearch((i, j), lines)
        print(xmasCnt)


part1()
