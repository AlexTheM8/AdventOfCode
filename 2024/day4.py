import numpy as np
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


SEARCH_ORDER = ['X', 'M', 'A', 'S']


def localSearch(coord, searchSpace, searchIdx, direction=None):
    x, y = coord
    width, height = searchSpace.shape
    match direction:
        case DirOptions.DIAG_UP_LEFT:
            if x == 0 or y == 0:
                return 0
            if searchSpace[x-1][y-1] == SEARCH_ORDER[searchIdx]:
                if searchIdx == len(SEARCH_ORDER) - 1:
                    return 1
                return localSearch((x-1, y-1), searchSpace, searchIdx + 1, direction=DirOptions.DIAG_UP_LEFT)
        case DirOptions.UP:
            if y == 0:
                return 0
            if searchSpace[x][y - 1] == SEARCH_ORDER[searchIdx]:
                if searchIdx == len(SEARCH_ORDER) - 1:
                    return 1
                return localSearch((x, y - 1), searchSpace, searchIdx + 1, direction=DirOptions.UP)
        case DirOptions.DIAG_UP_RIGHT:
            if y == 0 or x == width - 1:
                return 0
            if searchSpace[x + 1][y - 1] == SEARCH_ORDER[searchIdx]:
                if searchIdx == len(SEARCH_ORDER) - 1:
                    return 1
                return localSearch((x + 1, y - 1), searchSpace, searchIdx + 1, direction=DirOptions.DIAG_UP_RIGHT)
        case DirOptions.RIGHT:
            if x == width - 1:
                return 0
            if searchSpace[x + 1][y] == SEARCH_ORDER[searchIdx]:
                if searchIdx == len(SEARCH_ORDER) - 1:
                    return 1
                return localSearch((x + 1, y), searchSpace, searchIdx + 1, direction=DirOptions.RIGHT)
        case DirOptions.DIAG_DOWN_RIGHT:
            if x == width - 1 or y == height - 1:
                return 0
            if searchSpace[x + 1][y + 1] == SEARCH_ORDER[searchIdx]:
                if searchIdx == len(SEARCH_ORDER) - 1:
                    return 1
                return localSearch((x + 1, y + 1), searchSpace, searchIdx + 1, direction=DirOptions.DIAG_DOWN_RIGHT)
        case DirOptions.DOWN:
            if y == height - 1:
                return 0
            if searchSpace[x][y + 1] == SEARCH_ORDER[searchIdx]:
                if searchIdx == len(SEARCH_ORDER) - 1:
                    return 1
                return localSearch((x, y + 1), searchSpace, searchIdx + 1, direction=DirOptions.DOWN)
        case DirOptions.DIAG_DOWN_LEFT:
            if x == 0 or y == height - 1:
                return 0
            if searchSpace[x - 1][y + 1] == SEARCH_ORDER[searchIdx]:
                if searchIdx == len(SEARCH_ORDER) - 1:
                    return 1
                return localSearch((x - 1, y + 1), searchSpace, searchIdx + 1, direction=DirOptions.DIAG_DOWN_LEFT)
        case DirOptions.LEFT:
            if x == 0:
                return 0
            if searchSpace[x - 1][y] == SEARCH_ORDER[searchIdx]:
                if searchIdx == len(SEARCH_ORDER) - 1:
                    return 1
                return localSearch((x - 1, y), searchSpace, searchIdx + 1, direction=DirOptions.LEFT)
    return 0


def xSearch(coord, searchSpace):
    x, y = coord
    width, height = searchSpace.shape
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
    with open('2024/input/day4.txt', 'r') as f:
        lines = f.readlines()
        xmasCnt = 0
        np_arr = np.array([np.array([c for c in list(line.replace('\n', ''))]) for line in lines])
        for i, _ in enumerate(np_arr):
            for j, v in enumerate(np_arr[i]):
                if v != SEARCH_ORDER[0]:
                    continue
                for op in DirOptions:
                    xmasCnt += localSearch((i, j), np_arr, 1, direction=op)
        print(xmasCnt)


def part2():
    with open('2024/input/day4.txt', 'r') as f:
        lines = f.readlines()
        xmasCnt = 0
        np_arr = np.array([np.array([c for c in list(line.replace('\n', ''))]) for line in lines])
        for i, _ in enumerate(np_arr):
            for j, v in enumerate(np_arr[i]):
                # Search for A and xSearch
                if v != 'A':
                    continue
                xmasCnt += xSearch((i, j), np_arr)
        print(xmasCnt)


part2()
