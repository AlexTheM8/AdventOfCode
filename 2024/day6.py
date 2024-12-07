from enum import Enum

import numpy as np


class Direction(Enum):
    UP = 'u'
    RIGHT = 'r'
    DOWN = 'd'
    LEFT = 'l'


DIRECTION_LIST = [d for d in Direction]


def inBounds(pos, dims):
    x, y = pos
    w, h = dims
    if x < 0 or y < 0 or x >= w or y >= h:
        return False
    return True


def traverse(space, startPos):
    visited = set()
    direction = Direction.UP
    w, h = len(space), len(space[0])
    x, y = startPos
    x1, y1 = startPos
    while True:
        visited.add((x, y))
        match direction:
            case Direction.UP:
                x1 -= 1
            case Direction.RIGHT:
                y1 += 1
            case Direction.DOWN:
                x1 += 1
            case Direction.LEFT:
                y1 -= 1
        if not inBounds((x1, y1), (w, h)):
            return len(visited)
        if space[x1][y1] == '#':
            # Get next direction in list
            direction = DIRECTION_LIST[(DIRECTION_LIST.index(direction) + 1) % len(DIRECTION_LIST)]
            x1, y1 = x, y
        else:
            x, y = x1, y1


def part1():
    with open('./input/day6.txt') as f:
        lines = f.read().splitlines()
        startPos = None
        for i, line in enumerate(lines):
            if '^' in line:
                startPos = (i, line.index('^'))
                break
        visited = traverse(lines, startPos)
        print(visited)


def loops(space, startPos):
    visitedWithDir = set()
    direction = Direction.UP
    x, y = startPos
    while True:
        posWithDir = (x, y, direction)
        if posWithDir in visitedWithDir:
            return True
        col = space[:, y]
        row = space[x, :]
        visitedWithDir.add(posWithDir)
        match direction:
            case Direction.UP:
                search = col[:x]
                if '#' not in search:
                    return False
                search = np.flip(search)
                steps = np.where(search == '#')[0][0]
                x -= steps
            case Direction.RIGHT:
                search = row[y + 1:]
                if '#' not in search:
                    return False
                steps = np.where(search == '#')[0][0]
                y += steps
            case Direction.DOWN:
                search = col[x + 1:]
                if '#' not in col[x + 1:]:
                    return False
                steps = np.where(search == '#')[0][0]
                x += steps
            case Direction.LEFT:
                search = row[:y]
                if '#' not in search:
                    return False
                search = np.flip(search)
                steps = np.where(search == '#')[0][0]
                y -= steps
        direction = DIRECTION_LIST[(DIRECTION_LIST.index(direction) + 1) % len(DIRECTION_LIST)]


def part2():
    with open('./input/day6.txt') as f:
        lines = f.read().splitlines()
        blockOptions = 0
        npArr = np.array([[c for c in line] for line in lines])
        startPos = np.argwhere(npArr == '^')[0]
        for (i, j) in np.argwhere(npArr == '.'):
            newSpace = npArr.copy()
            newSpace[i][j] = '#'
            if loops(newSpace, startPos):
                blockOptions += 1
        print(blockOptions)


part2()
