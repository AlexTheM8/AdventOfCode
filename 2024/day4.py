from enum import Enum


class DirOptions(Enum):
    DIAG_UP_LEFT = 'dul'
    UP = 'u'
    DIAG_UP_RIGHT = 'dur'
    RIGHT = 'r'
    DIAG_DOWN_RIGHT = 'ddr'
    DOWN = 'd'
    DIAG_DOWN_LEFT = 'ddl'
    LEFT = 'l'


SEARCH_STRING = 'XMAS'


def localSearch(coord, searchSpace, searchIdx, direction=None):
    x, y = coord
    width, height = len(searchSpace), len(searchSpace[0])
    match direction:
        case DirOptions.DIAG_UP_LEFT:
            if x == 0 or y == 0:
                return 0
            if searchSpace[x-1][y-1] == SEARCH_STRING[searchIdx]:
                if searchIdx == len(SEARCH_STRING) - 1:
                    return 1
                return localSearch((x-1, y-1), searchSpace, searchIdx + 1, direction=DirOptions.DIAG_UP_LEFT)
        case DirOptions.UP:
            if y == 0:
                return 0
            if searchSpace[x][y - 1] == SEARCH_STRING[searchIdx]:
                if searchIdx == len(SEARCH_STRING) - 1:
                    return 1
                return localSearch((x, y - 1), searchSpace, searchIdx + 1, direction=DirOptions.UP)
        case DirOptions.DIAG_UP_RIGHT:
            if y == 0 or x == width - 1:
                return 0
            if searchSpace[x + 1][y - 1] == SEARCH_STRING[searchIdx]:
                if searchIdx == len(SEARCH_STRING) - 1:
                    return 1
                return localSearch((x + 1, y - 1), searchSpace, searchIdx + 1, direction=DirOptions.DIAG_UP_RIGHT)
        case DirOptions.RIGHT:
            if x == width - 1:
                return 0
            if searchSpace[x + 1][y] == SEARCH_STRING[searchIdx]:
                if searchIdx == len(SEARCH_STRING) - 1:
                    return 1
                return localSearch((x + 1, y), searchSpace, searchIdx + 1, direction=DirOptions.RIGHT)
        case DirOptions.DIAG_DOWN_RIGHT:
            if x == width - 1 or y == height - 1:
                return 0
            if searchSpace[x + 1][y + 1] == SEARCH_STRING[searchIdx]:
                if searchIdx == len(SEARCH_STRING) - 1:
                    return 1
                return localSearch((x + 1, y + 1), searchSpace, searchIdx + 1, direction=DirOptions.DIAG_DOWN_RIGHT)
        case DirOptions.DOWN:
            if y == height - 1:
                return 0
            if searchSpace[x][y + 1] == SEARCH_STRING[searchIdx]:
                if searchIdx == len(SEARCH_STRING) - 1:
                    return 1
                return localSearch((x, y + 1), searchSpace, searchIdx + 1, direction=DirOptions.DOWN)
        case DirOptions.DIAG_DOWN_LEFT:
            if x == 0 or y == height - 1:
                return 0
            if searchSpace[x - 1][y + 1] == SEARCH_STRING[searchIdx]:
                if searchIdx == len(SEARCH_STRING) - 1:
                    return 1
                return localSearch((x - 1, y + 1), searchSpace, searchIdx + 1, direction=DirOptions.DIAG_DOWN_LEFT)
        case DirOptions.LEFT:
            if x == 0:
                return 0
            if searchSpace[x - 1][y] == SEARCH_STRING[searchIdx]:
                if searchIdx == len(SEARCH_STRING) - 1:
                    return 1
                return localSearch((x - 1, y), searchSpace, searchIdx + 1, direction=DirOptions.LEFT)
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
                if c != SEARCH_STRING[0]:
                    continue
                for op in DirOptions:
                    xmasCnt += localSearch((i, j), lines, 1, direction=op)
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


part2()
