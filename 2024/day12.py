from enum import Enum
import numpy as np
from collections import defaultdict


with open('./input/day12.txt') as f:
    lines = f.read().splitlines()
plants = set(''.join(lines))
garden = np.array([[c for c in line] for line in lines])
w, h = garden.shape


class Direction(Enum):
    UP = 'u'
    RIGHT = 'r'
    DOWN = 'd'
    LEFT = 'l'


DIR_PAIR = (Direction.RIGHT, Direction.LEFT)


def setRegion(coord, plant, traversed=None):
    if traversed is None:
        traversed = {coord}
    traversed.add(coord)
    # Check neighbors
    for d in Direction:
        x, y = coord
        match d:
            case Direction.UP:
                x -= 1
            case Direction.RIGHT:
                y += 1
            case Direction.DOWN:
                x += 1
            case Direction.LEFT:
                y -= 1
        if not (0 <= x < w and 0 <= y < h) or garden[x, y] != plant:
            continue
        if (x, y) not in traversed:
            traversed.update(setRegion((x, y), plant, traversed))
    return traversed


def getRegions(plant):
    regions = []
    for x, y in np.argwhere(garden == plant):
        x = int(x)
        y = int(y)
        accounted = False
        for r in regions:
            if (x, y) in r:
                accounted = True
                break
        if not accounted:
            regions.append(setRegion((x, y), plant))
    return regions


def countPerim(coord):
    plant = garden[coord]
    perim = 0
    for d in Direction:
        x, y = coord
        match d:
            case Direction.UP:
                x -= 1
            case Direction.RIGHT:
                y += 1
            case Direction.DOWN:
                x += 1
            case Direction.LEFT:
                y -= 1
        if not (0 <= x < w and 0 <= y < h) or garden[x, y] != plant:
            perim += 1
    return perim


def part1():
    total = 0
    for p in plants:
        total += sum(len(r) * sum(countPerim(coord) for coord in r) for r in getRegions(p))
    print(total)


def checkOffNeighbors(coord, direction, section, visited):
    toCheck = [coord]
    while toCheck:
        x, y = toCheck.pop()
        c1 = (x+1, y) if direction in DIR_PAIR else (x, y+1)
        c2 = (x-1, y) if direction in DIR_PAIR else (x, y-1)
        if c1 in section and c1 not in visited:
            toCheck.append(c1)
            visited.add(c1)
        if c2 in section and c2 not in visited:
            toCheck.append(c2)
            visited.add(c2)


def countSides(region):
    sides = defaultdict(set)
    for coord in region:
        for d in Direction:
            x, y = coord
            match d:
                case Direction.UP:
                    x -= 1
                case Direction.RIGHT:
                    y += 1
                case Direction.DOWN:
                    x += 1
                case Direction.LEFT:
                    y -= 1
            pos = y if d in DIR_PAIR else x
            if (x, y) not in region:
                sides[pos, d].add((x, y))
    sideCount = 0
    for (_, direction), section in sides.items():
        visited = set()
        for coord in section:
            if coord not in visited:
                visited.add(coord)
                checkOffNeighbors(coord, direction, section, visited)
                sideCount += 1
    return sideCount


def part2():
    total = 0
    for p in plants:
        for r in getRegions(p):
            if len(r) < 3:
                total += len(r) * 4
            else:
                total += len(r) * countSides(r)
    print(total)


part2()
