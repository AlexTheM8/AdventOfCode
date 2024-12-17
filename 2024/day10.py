from enum import Enum

import numpy as np


class Direction(Enum):
    UP = 'u'
    RIGHT = 'r'
    DOWN = 'd'
    LEFT = 'l'


trail = np.array([[]])


def traversePath(currLoc):
    currHeight = int(trail[currLoc])
    if currHeight == 9:
        return [currLoc], 1
    endpoints, paths = set(), 0
    w, h = trail.shape
    for d in Direction:
        x, y = currLoc
        match d:
            case Direction.LEFT:
                y -= 1
            case Direction.DOWN:
                x += 1
            case Direction.RIGHT:
                y += 1
            case Direction.UP:
                x -= 1
        if not (0 <= x < w and 0 <= y < h):
            continue
        nextStep = trail[x, y]
        if nextStep == '.' or int(nextStep) != currHeight+1:
            continue
        e, p = traversePath((x, y))
        paths += p
        endpoints.update(e)
    return endpoints, paths


def part1and2(part2=False):
    global trail
    with open('./input/day10.txt') as f:
        lines = f.read().splitlines()
        trail = np.array([[c for c in line] for line in lines])
        score = 0
        for x, y in np.argwhere(trail == '0'):
            endpoints, paths = traversePath((x, y))
            score += paths if part2 else len(endpoints)
        print(score)


part1and2(part2=True)
